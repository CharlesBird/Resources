import requests
from requests.auth import HTTPBasicAuth
from requests_ntlm import HttpNtlmAuth
import xmltodict
import json

url = "http://172.70.0.91:8099/api/Query/RMS_Customer_BC?company=1000"

data = {
    "startingPosition": 1,
    "numberOfRecordsToFetch": 400
}

res = requests.get(url, auth=HTTPBasicAuth('shruntong\Barcode', 'B.rms123'), params=data, headers={"Content-Type": "text/plain"})
print(res.status_code)
print(res.text)


# if __name__ == '__main__':
#     data = '''
#         <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:dat="http://schemas.microsoft.com/dynamics/2010/01/datacontracts" xmlns:arr="http://schemas.microsoft.com/2003/10/Serialization/Arrays" xmlns:tem="http://tempuri.org" xmlns:quer="http://schemas.microsoft.com/dynamics/2006/02/documents/QueryCriteria">
#            <soapenv:Header>
#               <dat:CallContext>
#                  <!--Optional:-->
#                  <dat:Company>1000</dat:Company>
#                  <!--Optional:-->
#                  <dat:Language>en-us</dat:Language>
#                  <!--Optional:-->
#                  <dat:LogonAsUser></dat:LogonAsUser>
#                  <!--Optional:-->
#                  <dat:MessageId></dat:MessageId>
#                  <!--Optional:-->
#                  <dat:PartitionKey></dat:PartitionKey>
#                  <!--Optional:-->
#                  <dat:PropertyBag>
#                     <!--Zero or more repetitions:-->
#                     <arr:KeyValueOfstringstring>
#                        <arr:Key></arr:Key>
#                        <arr:Value></arr:Value>
#                     </arr:KeyValueOfstringstring>
#                  </dat:PropertyBag>
#               </dat:CallContext>
#            </soapenv:Header>
#            <soapenv:Body>
#               <tem:RMS_CustTableServiceFindRequest>
#                  <!--Optional:-->
#                  <quer:QueryCriteria>
#                     <quer:CriteriaElement>
#                        <quer:DataSourceName>CustTable</quer:DataSourceName>
#                        <quer:FieldName>AccountNum</quer:FieldName>
#                        <quer:Operator>equal</quer:Operator>
#                        <quer:Value1>C000650525</quer:Value1>
#                        <!--Optional:-->
#                        <quer:Value2></quer:Value2>
#                     </quer:CriteriaElement>
#                  </quer:QueryCriteria>
#               </tem:RMS_CustTableServiceFindRequest>
#            </soapenv:Body>
#         </soapenv:Envelope>'''
#     headers = [("SOAPAction", "http://tempuri.org/RMS_CustTableService/find"),
#                ("Content-Type", "text/xml;charset=utf-8")]
#     url = "http://172.70.0.49:801/MicrosoftDynamicsAXAif60/RMSCustTable/xppservice.svc"
#
#     res = requests.post(url, auth=HttpNtlmAuth('shruntong\Barcode', 'B.rms123'), data=data, headers=dict(headers))
#     print(res.request.headers)
#     print(res.status_code)
#     print(res.text)