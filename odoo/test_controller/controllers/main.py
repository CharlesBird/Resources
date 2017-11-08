# -*- coding: utf-8 -*-
from openerp import http, SUPERUSER_ID
from openerp.http import request
import datetime
import time
import json
import hmac
import hashlib
# from openerp.tools import consteq

import logging
_logger = logging.getLogger(__name__)


class TestController(http.Controller):

    @http.route(['/test/1.0/index/'], type='http', auth='none', csrf=False)
    def index(self, db=None, redirect=None, **k):
        # import pdb
        # pdb.set_trace()
        data = request.httprequest.method == 'POST' and json.loads(request.httprequest.data) or k
        # email, token = data.get('email', ''), data.get('token', '')
        # self.verify_token(email, token)
        # request.session.authenticate(request.session.db, 'support@unovo.com.cn', 'unovo883&')
        # uid = request.env['res.users'].sudo().search([('login', '=', data['email'])]).id
        # request.session.login = data['email']
        # request.session.uid = uid
        # request.session.password = '1'
        uid = request.session.authenticate(request.session.db, data['email'], '1234567890')
        if uid is not False:
            request.params['login_success'] = True
            if not redirect:
                redirect = '/web'
            return http.redirect_with_hash(redirect)
        res = request.make_response('Hello World', headers=[('Access-Control-Allow-Origin', '*'), ('Access-Control-Allow-Headers', '*'), ('Access-Control-Allow-Methods', '*')])

        return res

    # @http.route(['/test/1.0/token/'], type='http', auth='none', csrf=False)
    # def token(self, db=None, **k):
    #     # import pdb
    #     # pdb.set_trace()
    #     data = request.httprequest.method == 'POST' and json.loads(request.httprequest.data) or k
    #     email, time_limit = data.get('email', ''), int(data.get('time_limit', 3600*2))
    #     assert email, "Token protection requires a email"
    #     max_ts = '' if not time_limit else int(time.time() + time_limit)
    #     msg = '%s%s' % (email, max_ts)
    #     secret = request.env['ir.config_parameter'].sudo().get_param('database.secret')
    #     assert secret, "Token protection requires a configured database secret"
    #     hm = hmac.new(str(secret), msg, hashlib.sha1).hexdigest()
    #     result = '%so%s' % (hm, max_ts)
    #     # 验证是否是合法url
    #     # url = request.httprequest.headers.get('Origin') or ''
    #     # urls = [unovo_url['url'] for unovo_url in request.registry['unovo.url'].search_read(request.cr, SUPERUSER_ID, [], ['url'])]
    #     # if url not in urls:
    #     #     code_dict.update({1002: url})
    #     return request.make_response(result, headers=[('Access-Control-Allow-Origin', '*'), ('Access-Control-Allow-Headers', '*'), ('Access-Control-Allow-Methods', '*')])

    # def verify_token(self, email, token):
    #     if not token:
    #         return False
    #     try:
    #         hm, _, max_ts = str(token).rpartition('o')
    #     except UnicodeEncodeError:
    #         return False
    #     if max_ts:
    #         try:
    #             if int(max_ts) < int(time.time()):
    #                 return False
    #         except ValueError:
    #             return False
    #     msg = '%s%s' % (token, max_ts)
    #     secret = self.env['ir.config_parameter'].sudo().get_param('database.secret')
    #     assert secret, "Token protection requires a configured database secret"
    #     hm_expected = hmac.new(str(secret), msg, hashlib.sha1).hexdigest()
    #     return consteq(hm, hm_expected)
