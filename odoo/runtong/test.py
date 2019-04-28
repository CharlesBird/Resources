from suds.client import Client

url = 'http://axdev:8101/DynamicsAx/Services/QueryService'

client = Client(url)
# print(client)

# import ldap, json
#
# # client = Client()
#
# def ldap_login(ldap_path, user, domain, passwd):
#     try:
#         c = ldap.initialize(ldap_path)
#         c.protocol_version = ldap.VERSION3
#         d = c.simple_bind("%s@%s"%(user, domain), passwd)
#     except ldap.INVALID_CREDENTIALS as e:
#         c.unbind()
#         c = d = None
#     finally:
#         return c, d
#
#
# def user_info(c, user, base):
#     try:
#         scope = ldap.SCOPE_SUBTREE
#         filterstr = "(sAMAccountName=%s)"%user
#
#         id = c.search(base, scope, filterstr, None)
#
#         result_type, result_data = c.result(id, 1)
#         return result_data
#     except ldap.LDAPError as e:
#         return None
#     finally:
#         pass
#
# ####
#
# ldap_path = "ldap://139.219.129.144:80"
# base = "DC=dev,DC=com"
# user = "shruntong\Barcode"
# domain = "172.70.0.4";
# passwd = "B.rms123";
#
# c, d = ldap_login(ldap_path, user, domain, passwd)
#
# if c == None:
#     print("login error!")
#     exit(1)
#
# print("user: %s login ok!"%user)
# info = user_info(c, user, base)
# print(json.dumps(info, ensure_ascii=False, indent=4))
#
# c.unbind()

import sys

# import ldap, logging, time
#
# logfile = 'e:\\a.txt'
# # logging.basicConfig(filename=logfile,level=logging.INFO)
# # logging.basicConfig(format='%(time.asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.basicConfig(level=logging.INFO,
#                     # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', #返回值：Thu, 26 May 2016 15:09:31 t11.py[line:92] INFO
#                     format='%(asctime)s %(levelname)s %(message)s',
#                     # datefmt='%a, %d %b %Y %H:%M:%S',
#                     # datefmt='%Y/%m/%d %I:%M:%S %p', #返回2016/05/26 03:12:56 PM
#                     datefmt='%Y-%m-%d %H:%M:%S',  # 返回2016/05/26 03:12:56 PM
#                     filename=logfile  # ,
#                     # filemode='a' #默认为a
#                     )
#
#
# # logging输出结果：
# # 2016-05-26 15:22:29 INFO liu1 valid passed.
# # 2016-05-26 15:22:37 INFO liu1 valid passed.
#
#
# class ldapc:
#     def __init__(self, ldap_path, baseDN, ldap_authuser, ldap_authpass):
#         self.baseDN = baseDN
#         self.ldap_error = None
#         self.l = ldap.initialize(ldap_path)
#         self.l.protocol_version = ldap.VERSION3
#         print('url:', ldap_path)
#         print('username:', ldap_authuser)
#         print('password:', ldap_authpass)
#         try:
#             res = self.l.simple_bind_s(ldap_authuser, ldap_authpass)
#             print(res)
#         except ldap.LDAPError as err:
#             self.ldap_error = 'Connect to %s failed, Error:%s.' % (ldap_path, err.message['desc'])
#             print(self.ldap_error)
#         # finally:
#         #     self.l.unbind_s()
#         #     del self.l
#
#     def search_users(self, username):  # 模糊查找，返回一个list，使用search_s()
#         if self.ldap_error is None:
#             try:
#                 searchScope = ldap.SCOPE_SUBTREE
#                 searchFiltername = "sAMAccountName"  # 通过samaccountname查找用户
#                 retrieveAttributes = None
#                 searchFilter = '(' + searchFiltername + "=" + username + '*)'
#                 ldap_result = self.l.search_s(self.baseDN, searchScope, searchFilter, retrieveAttributes)
#                 if len(ldap_result) == 0:  # ldap_result is a list.
#                     return "%s doesn't exist." % username
#                 else:
#                     # result_type, result_data = self.l.result(ldap_result, 0)
#                     # return result_type, ldap_result
#                     return ldap_result
#             except ldap.LDAPError as err:
#                 return err
#
#     def search_user(self, username):  # 精确查找，返回值为list，使用search()
#         if self.ldap_error is None:
#             try:
#                 searchScope = ldap.SCOPE_SUBTREE
#                 searchFiltername = "sAMAccountName"  # 通过samaccountname查找用户
#                 retrieveAttributes = None
#                 searchFilter = '(' + searchFiltername + "=" + username + ')'
#                 ldap_result_id = self.l.search(self.baseDN, searchScope, searchFilter, retrieveAttributes)
#                 result_type, result_data = self.l.result(ldap_result_id, 0)
#                 if result_type == ldap.RES_SEARCH_ENTRY:
#                     return result_data
#                 else:
#                     return "%s doesn't exist." % username
#             except ldap.LDAPError as err:
#                 return err
#
#     def search_userDN(self, username):  # 精确查找，最后返回该用户的DN值
#         if self.ldap_error is None:
#             try:
#                 searchScope = ldap.SCOPE_SUBTREE
#                 searchFiltername = "sAMAccountName"  # 通过samaccountname查找用户
#                 retrieveAttributes = None
#                 searchFilter = '(' + searchFiltername + "=" + username + ')'
#                 ldap_result_id = self.l.search(self.baseDN, searchScope, searchFilter, retrieveAttributes)
#                 result_type, result_data = self.l.result(ldap_result_id, 0)
#                 if result_type == ldap.RES_SEARCH_ENTRY:
#                     print('flag:', 1)
#                     return result_data[0][0]  # list第一个值为用户的DN，第二个值是一个dict，包含了用户属性信息
#                 else:
#                     print('flag:', 0)
#                     return "%s doesn't exist." % username
#             except ldap.LDAPError as err:
#                 return err
#
#     def valid_user(self, username, userpassword):  # 验证用户密码是否正确
#         if self.ldap_error is None:
#             target_user = self.search_userDN(username)  # 使用前面定义的search_userDN函数获取用户的DN
#             if target_user.find("doesn't exist") == -1:
#                 try:
#                     self.l.simple_bind_s(target_user, userpassword)
#                     logging.info('%s valid passed.\r' % (username))  # logging会自动在每行log后面添加"\000"换行，windows下未自动换行
#                     return True
#                 except ldap.LDAPError as err:
#                     return err
#             else:
#                 return target_user
#
#     def update_pass(self, username, oldpassword, newpassword):  #####未测试#########
#         if self.ldap_error is None:
#             target_user = self.search_userDN(username)
#             if target_user.find("doesn't exist") == -1:
#                 try:
#                     self.l.simple_bind_s(target_user, oldpassword)
#                     self.l.passwd_s(target_user, oldpassword, newpassword)
#                     return 'Change password success.'
#                 except ldap.LDAPError as err:
#                     return err
#             else:
#                 return target_user
#
#
# ldap_authuser = 'shruntong\Barcode'
# ldap_authpass = 'B.rms123'
# domainname = '172.70.0.4'
# ldappath = 'ldap://139.219.129.144:389'
#
# baseDN = 'DC=xxx,DC=com'  # ldap_authuser在连接到LDAP的时候不会用到baseDN，在验证其他用户的时候才需要使用
# username = 'xxx'  # 要查找/验证的用户
# p = ldapc(ldappath, baseDN, ldap_authuser, ldap_authpass)
# # print 'list--search:',p.search_users(username)
# print('DN----search', p.search_userDN(username))
# print('DN-ty', type(p.search_userDN(username)))
# print('user--valid', p.valid_user(ldap_authuser, ldap_authpass))  # 调用valid_user()方法验证用户是否为合法用户