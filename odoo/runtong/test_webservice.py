from suds.client import Client
from suds.transport.http import HttpAuthenticated
import base64
import urllib3
import urllib.request
from suds.xsd.doctor import Import, ImportDoctor


if __name__ == '__main__':
    # res = requests.get('http://axdev:801/MicrosoftDynamicsAXAif60/test5/xppservice.svc')
    # print(res.status_code)
    url = 'http://172.70.0.49:801/MicrosoftDynamicsAXAif60/test5/xppservice.svc?wsdl'
    # # url = 'http://track.tcs.com.pk/trackingaccount/track.asmx?WSDL'
    # imp = Import('http://www.w3.org/2001/XMLSchema', location='https://www.w3.org/2001/XMLSchema.dtd')
    # imp.filter.add('http://WebXml.com.cn/')
    # doctor = ImportDoctor(imp)
    t = HttpAuthenticated(username='shruntong\Barcode', password='B.rms123')
    t.handler = urllib.request.HTTPBasicAuthHandler(t.pm)
    t.urlopener = urllib.request.build_opener(t.handler)
    # base64str = base64.encodebytes(b'shruntong\Barcode:B.rms123')
    # print(base64str[:-1])
    # s = base64str.decode('utf-8')
    # print(s)
    # authenticationHeader = {
    #     "SOAPAction": "ActionName",
    #     "Authorization": "Basic %s" % base64str.decode('utf-8').replace('\n', '')
    # }
    # print(authenticationHeader)
    client = Client(url, transport=t)
    print(client)