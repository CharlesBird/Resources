import requests
from requests.auth import HTTPBasicAuth
from requests_ntlm import HttpNtlmAuth
import xmltodict
import json

url = "http://172.70.0.91:8099/api/Query/RMS_WMSLocation"

data = {
    "startingPosition": 20,
    "numberOfRecordsToFetch": 500
}

res = requests.get(url, auth=HTTPBasicAuth('shruntong\Barcode', 'B.rms123'), params=data, headers={"Content-Type": "text/plain"})
print(res.status_code)
print(res.text)
if "MaxReceivedMessageSize" in res.text:
    print(1111)
# json_res = json.loads(res.text)
# print(json_res)
# print(len(json_res['RMS_QueryService']['WMSLocation']))


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
#               <tem:RMS_WMSLocationServiceFindRequest>
#                  <!--Optional:-->
#                  <quer:QueryCriteria>
#                     <quer:CriteriaElement>
#                        <quer:DataSourceName>WMSLocation</quer:DataSourceName>
#                        <quer:FieldName>WMSLocationId</quer:FieldName>
#                        <quer:Operator>equal</quer:Operator>
#                        <quer:Value1>WV3-3-4</quer:Value1>
#                        <!--Optional:-->
#                        <quer:Value2></quer:Value2>
#                     </quer:CriteriaElement>
#
#                  </quer:QueryCriteria>
#               </tem:RMS_WMSLocationServiceFindRequest>
#            </soapenv:Body>
#         </soapenv:Envelope>'''
#     headers = [("SOAPAction", "http://tempuri.org/RMS_WMSLocationService/find"),
#                ("Content-Type", "text/xml;charset=utf-8")]
#     url = "http://172.70.0.49:801/MicrosoftDynamicsAXAif60/RMSWMSLocation/xppservice.svc"
#
#     res = requests.post(url, auth=HttpNtlmAuth('shruntong\Barcode', 'B.rms123'), data=data, headers=dict(headers))
#     print(res.request.headers)
#     print(res.status_code)
#     print(res.text)