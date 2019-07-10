# odoo.service.server: Thread <Thread(odoo.service.http.request.140501351036672, started 140501351036672)> virtual real time limit (120/120s) reached.
import xmlrpclib

# url, db, username, password = 'http://localhost:8069', 'rt_demo', 'admin', '1'
url, db, username, password = 'http://192.168.11.137:8069', 'shrt', 'admin', 'admin'
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url), allow_none=True)
# res = models.execute_kw(db, uid, password, 'ax.sync.config', 'button_batch_synchronize_create', [[14]])
res = models.execute_kw(db, uid, password, 'product.product', 'update_translate_name', [])
print res