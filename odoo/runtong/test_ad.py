from ldap3 import Server
from ldap3 import Server, Connection, ALL
server = Server('172.70.0.4',get_info=ALL)
conn = Connection(server, 'shruntong\Barcode','B.rms123')
conn.bind()
res = conn.search('dc=shruntong,dc=com', '(objectclass=user)')
conn.entries