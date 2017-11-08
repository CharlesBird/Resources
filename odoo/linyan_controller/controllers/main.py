# -*- coding: utf-8 -*-
from openerp import http, SUPERUSER_ID
from openerp.http import request
from openerp.exceptions import Warning, except_orm
import datetime
import time
import json
import hmac
import hashlib
from openerp.tools import consteq

import logging
_logger = logging.getLogger(__name__)


class LynynController(http.Controller):

    # @http.route(['/test/1.0/index/'], type='http', auth='none', csrf=False)
    # def index(self, db=None, redirect=None, **k):
    #     import pdb
    #     pdb.set_trace()
    #     data = request.httprequest.method == 'POST' and json.loads(request.httprequest.data) or k
    #     email, token = data.get('email', ''), data.get('token', '')
    #     self.verify_token(email, token)
    #     uid = request.env['res.users'].sudo().search([('login', '=', data['email'])]).id
    #     request.session.login = data['email']
    #     request.session.uid = uid
    #     # uid = request.session.authenticate(request.session.db, 'test@qq.com', '1')
    #     if uid is not False:
    #         request.params['login_success'] = True
    #         if not redirect:
    #             redirect = '/web'
    #         return http.redirect_with_hash(redirect)
    #     res = request.make_response('Hello World', headers=[('Access-Control-Allow-Origin', '*'), ('Access-Control-Allow-Headers', '*'), ('Access-Control-Allow-Methods', '*')])

    #     return res

    @http.route(['/oa/v1.0/token/'], type='http', auth='none', csrf=False)
    def token(self, db=None, **k):
        result = {}
        data = request.httprequest.method == 'POST' and json.loads(request.httprequest.data) or k
        email, time_limit = data.get('email', ''), int(data.get('time_limit', 3600*2))
        try:
            if not email:
                raise except_orm(('Error'), ('Token protection requires a email.'))
            if not data.get('secret', ''):
                raise except_orm(('Error'), ('Token protection requires a secret.'))
            # 验证是否是合法secret
            secret = request.env['ir.config_parameter'].sudo().get_param('database.secret')
            if secret != data.get('secret', ''):
                raise except_orm(('Error'), ('Error secret.'))
            result = {"code": 1, "message": self._get_token(email, time_limit)}
        except Exception, e:
            result = {"code": 0, "message": e.value}
        # 验证是否是合法url
        url = request.httprequest.headers.get('Origin') or ''
        _logger.info('http url from dingding origin: %s' % url)
        # urls = [unovo_url['url'] for unovo_url in request.registry['unovo.url'].search_read(request.cr, SUPERUSER_ID, [], ['url'])]
        # if url not in urls:
        #     code_dict.update({1002: url})
        return request.make_response(json.dumps(result), headers=[('Access-Control-Allow-Origin', '*'), ('Access-Control-Allow-Headers', '*'), ('Access-Control-Allow-Methods', '*')])

    def _get_token(self, *args):
        email, time_limit = args
        users = request.env['res.users'].sudo().search([('email', '=', email)])
        max_ts = '' if not time_limit else int(time.time() + time_limit)
        msg = '%s%s' % (email, max_ts)
        secret = request.env['ir.config_parameter'].sudo().get_param('database.secret')
        hm = hmac.new(str(secret), msg, hashlib.sha1).hexdigest()
        result = '%so%s' % (hm, max_ts)
        users.write({'u_token': result})
        return result

    def verify_token(self, u_token):
        if not u_token:
            return False
        try:
            hm, _, max_ts = str(u_token).rpartition('o')
        except UnicodeEncodeError:
            return False
        if max_ts:
            try:
                if int(max_ts) < int(time.time()):
                    return False
            except ValueError:
                return False
        users = request.env['res.users'].sudo().search_read([('u_token', '=', u_token)], ['email'])
        if not users:
            return False
        msg = '%s%s' % (users[0]['email'], max_ts)
        secret = request.env['ir.config_parameter'].sudo().get_param('database.secret')
        assert secret, "Token protection requires a configured database secret"
        hm_expected = hmac.new(str(secret), msg, hashlib.sha1).hexdigest()
        return consteq(hm, hm_expected)

    @http.route(['/oa/v1.0/lynyn/'], type='http', auth='none', csrf=False)
    def lynyn(self, db=None, redirect=None, **k):
        data = request.httprequest.method == 'POST' and json.loads(request.httprequest.data) or k
        u_token = data.get('token', '')
        if not self.verify_token(u_token):
            return request.make_response('Not found', headers=[('Access-Control-Allow-Origin', '*'), ('Access-Control-Allow-Headers', '*'), ('Access-Control-Allow-Methods', '*')])
        users = request.env['res.users'].sudo().search_read([('u_token', '=', u_token)], ['email'])
        uid = request.session.authenticate(db, users[0]['email'], u_token)
        if uid is not False:
            request.params['login_success'] = True
            if not redirect:
                redirect = '/web'
            return http.redirect_with_hash(redirect)

    @http.route(['/oa/v1.0/lynyn/users'], type='http', auth='none', csrf=False)
    def lynyn_users(self, db=None, **k):
        data = request.httprequest.method == 'POST' and json.loads(request.httprequest.data) or k
        dbs = {'linyan_dev': u'上海林炎工贸有限公司', 'liufang_dev': u'宁波六方化工有限公司', 'hklinyan_dev': u'香港林炎工贸有限公司'}
        secret = request.env['ir.config_parameter'].sudo().get_param('database.secret')
        assert secret, "Token protection requires a configured database secret"
        if not secret == data.get('secret', ''):
            return request.make_response(json.dumps({"code": 1, "message": 'Error secret'}), headers=[('Access-Control-Allow-Origin', '*'), ('Access-Control-Allow-Headers', '*'), ('Access-Control-Allow-Methods', '*')])
        users = request.env['res.users'].sudo().search_read(['|', ('active', '=', True), ('active', '=', False)], ['email', 'active', 'mobile'])
        result = {'users': users, 'db': db, 'dbname': dbs.get(db, db)}
        return request.make_response(json.dumps(result), headers=[('Access-Control-Allow-Origin', '*'), ('Access-Control-Allow-Headers', '*'), ('Access-Control-Allow-Methods', '*')])

    @http.route(['/oa/v1.0/lynyn/dingding/admin'], type='http', auth='none', csrf=False)
    def lynyn_dingding_admin(self, db=None, **k):
        data = request.httprequest.method == 'POST' and json.loads(request.httprequest.data) or k
        secret = request.env['ir.config_parameter'].sudo().get_param('database.secret')
        assert secret, "Token protection requires a configured database secret"
        if not secret == data.get('secret', ''):
            return request.make_response(json.dumps({"code": 1, "message": 'Error secret'}), headers=[('Access-Control-Allow-Origin', '*'), ('Access-Control-Allow-Headers', '*'), ('Access-Control-Allow-Methods', '*')])
        users = request.env['res.users'].sudo().search([('id', '=', data.get('id', False))])
        result = {"button_admin": False}
        if users.has_group('linyan_controller.group_linyan_dingding_admin'):
            result.update({"button_admin": True})
        return request.make_response(json.dumps(result), headers=[('Access-Control-Allow-Origin', '*'), ('Access-Control-Allow-Headers', '*'), ('Access-Control-Allow-Methods', '*')])
