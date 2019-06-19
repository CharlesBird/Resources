import requests
from requests_ntlm import HttpNtlmAuth
from lxml import etree
import xmltodict
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # data = '''
    # <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:dat="http://schemas.microsoft.com/dynamics/2010/01/datacontracts" xmlns:arr="http://schemas.microsoft.com/2003/10/Serialization/Arrays" xmlns:ser="http://schemas.microsoft.com/dynamics/2008/01/services" xmlns:quer="http://schemas.microsoft.com/dynamics/2006/02/documents/QueryCriteria">
    #     <soapenv:Header>
    #         <dat:CallContext>
    #         <!--Optional:-->
    #         <dat:Company>1000</dat:Company>
    #         <!--Optional:-->
    #         <dat:Language>en-us</dat:Language>
    #         <!--Optional:-->
    #         <dat:LogonAsUser></dat:LogonAsUser>
    #         <!--Optional:-->
    #         <dat:MessageId></dat:MessageId>
    #         <!--Optional:-->
    #         <dat:PartitionKey></dat:PartitionKey>
    #         <!--Optional:-->
    #             <dat:PropertyBag>
    #             <!--Zero or more repetitions:-->
    #             <arr:KeyValueOfstringstring>
    #             <arr:Key></arr:Key>
    #             <arr:Value></arr:Value>
    #             </arr:KeyValueOfstringstring>
    #             </dat:PropertyBag>
    #         </dat:CallContext>
    #     </soapenv:Header>
    #     <soapenv:Body>
    #     <ser:VendGroupServiceFindRequest>
    #     <!--Optional:-->
    #     <quer:QueryCriteria>
    #
    #     </quer:QueryCriteria>
    #     </ser:VendGroupServiceFindRequest>
    #     </soapenv:Body>
    # </soapenv:Envelope>'''
    # headers = [("SOAPAction", "http://schemas.microsoft.com/dynamics/2008/01/services/VendGroupService/find"),
    #            ("Content-Type", "text/xml;charset=utf-8")]
    # url = "http://172.70.0.49:801/MicrosoftDynamicsAXAif60/test5/xppservice.svc"

    data = '''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:dat="http://schemas.microsoft.com/dynamics/2010/01/datacontracts" xmlns:arr="http://schemas.microsoft.com/2003/10/Serialization/Arrays" xmlns:ser="http://schemas.microsoft.com/dynamics/2008/01/services" xmlns:quer="http://schemas.microsoft.com/dynamics/2006/02/documents/QueryCriteria">
       <soapenv:Header>
          <dat:CallContext>
             <!--Optional:-->
             <dat:Company>1000</dat:Company>
             <!--Optional:-->
             <dat:Language>en-us</dat:Language>
             <!--Optional:-->
             <dat:LogonAsUser></dat:LogonAsUser>
             <!--Optional:-->
             <dat:MessageId></dat:MessageId>
             <!--Optional:-->
             <dat:PartitionKey></dat:PartitionKey>
             <!--Optional:-->
             <dat:PropertyBag>
                <!--Zero or more repetitions:-->
                <arr:KeyValueOfstringstring>
                   <arr:Key></arr:Key>
                   <arr:Value></arr:Value>
                </arr:KeyValueOfstringstring>
             </dat:PropertyBag>
          </dat:CallContext>
       </soapenv:Header>
       <soapenv:Body>
          <ser:ItemServiceFindRequest>
             <!--Optional:-->
             <quer:QueryCriteria>
                <quer:CriteriaElement>
                   <quer:DataSourceName>InventTable</quer:DataSourceName>
                   <quer:FieldName>ItemId</quer:FieldName>
                   <quer:Operator>range</quer:Operator>
                   <quer:Value1>10001000067</quer:Value1>
                   <!--Optional:-->
                   <quer:Value2>10001000068</quer:Value2>
                </quer:CriteriaElement>
             </quer:QueryCriteria>
          </ser:ItemServiceFindRequest>
       </soapenv:Body>
    </soapenv:Envelope>'''
    headers = [("SOAPAction", "http://schemas.microsoft.com/dynamics/2008/01/services/ItemService/find"),
               ("Content-Type", "text/xml;charset=utf-8")]
    url = "http://172.70.0.49:801/MicrosoftDynamicsAXAif60/InventItem/xppservice.svc"

    res = requests.post(url, auth=HttpNtlmAuth('shruntong\Barcode', 'B.rms123'), data=data, headers=dict(headers))
    print(res.request.headers)
    print(res.status_code)
    print(res.text)
    doc = etree.fromstring(res.text)
    print(doc.tag, doc.nsmap)
    model_docs = doc.findall("{*}Body/{*}ItemServiceFindResponse/{*}Item/{*}InventTable")
    # print(model_docs.getchildren())
    for model_node in model_docs:
        if model_node.attrib.get('class') == 'entity':
            for field_node in model_node:
                # if field_node.endswith('ItemId'):

                print(field_node.tag, field_node.text)
    # soup = BeautifulSoup(res.text, features='xml')
    # xml = soup.find_all('InventTable')
    # for x in xml:
    #     for item in x.find_all():
    #         print(item.name, item.text)

    a = xmltodict.parse(res.text)
    print(dict(a))
    # node = doc.findall('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
    # ns = doc.nsmap['s']
    # ns = "{%s}" % ns
    # item = doc.find(ns + "Body")
    # print(item.text)
    # ns = doc.nsmap
    # print(ns)
    # t = doc.getroottree()
    # print(t.getchildren())
    # # print(doc.getroottree().tag)
    # for node in doc.iter(tag='{*}InventTable'):
    #     print(node.tag, node.text)

    # # url = 'http://track.tcs.com.pk/trackingaccount/track.asmx?WSDL'
    # imp = Import('http://www.w3.org/2001/XMLSchema', location='https://www.w3.org/2001/XMLSchema.dtd')
    # imp.filter.add('http://WebXml.com.cn/')
    # doctor = ImportDoctor(imp)
    # t.handler = urllib.request.HTTPBasicAuthHandler(t.pm)
    # t.urlopener = urllib.request.build_opener(t.handler)
    # base64str = base64.encodebytes(b'shruntong\Barcode:B.rms123')
    # print(base64str[:-1])
    # s = base64str.decode('utf-8')
    # print(s)
    # authenticationHeader = {
    #     "SOAPAction": "ActionName",
    #     "Authorization": "Basic %s" % base64str.decode('utf-8').replace('\n', '')
    # }
    # print(authenticationHeader)

    # username = 'shruntong\Barcode'
    # password = 'B.rms123'
    # domain = ''  # Can be blank if you are not in a domain
    # workstation = socket.gethostname().upper()  # Can be blank if you wish to not send this info
    #
    # ntlm_context = NtlmContext(username, password, domain, workstation,
    #                            ntlm_compatibility=0)  # Put the ntlm_compatibility level here, 0-2 for LM Auth/NTLMv1 Auth
    # negotiate_message = ntlm_context.step()
    # challenge_message = http.response.headers['HEADERFIELD']

    # authenticate_message = ntlm_context.step(challenge_message)
    # t = HttpAuthenticated(username='shruntong\Barcode', password='B.rms123')
    # ntlm.handler = urllib.request.HTTPBasicAuthHandler(ntlm.pm)
    # ntlm.urlopener = urllib.request.build_opener(ntlm.handler)

    # url = 'http://172.70.0.49:801/MicrosoftDynamicsAXAif60/test5/xppservice.svc?wsdl'
    # ntlm = WindowsHttpAuthenticated(username='shruntong\Barcode', password='B.rms123')
    # client = Client(url, transport=ntlm)
    # print(client)
