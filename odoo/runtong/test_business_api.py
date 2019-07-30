import requests
from requests_ntlm import HttpNtlmAuth
import xmltodict
import json


if __name__ == '__main__':
    data = '''
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:dat="http://schemas.microsoft.com/dynamics/2010/01/datacontracts" xmlns:arr="http://schemas.microsoft.com/2003/10/Serialization/Arrays" xmlns:tem="http://tempuri.org" xmlns:quer="http://schemas.microsoft.com/dynamics/2006/02/documents/QueryCriteria">
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
              <tem:RMS_DepartmentServiceFindRequest>
                 <!--Optional:-->
                 <quer:QueryCriteria>
        
                 </quer:QueryCriteria>
              </tem:RMS_DepartmentServiceFindRequest>
           </soapenv:Body>
        </soapenv:Envelope>'''
    headers = [("SOAPAction", "http://tempuri.org/RMS_DepartmentService/find"),
               ("Content-Type", "text/xml;charset=utf-8")]
    url = "http://172.70.0.49:801/MicrosoftDynamicsAXAif60/RMSDepartment/xppservice.svc"

    res = requests.post(url, auth=HttpNtlmAuth('shruntong\Barcode', 'B.rms123'), data=data, headers=dict(headers))
    print(res.request.headers)
    print(res.status_code)
    print(res.text)