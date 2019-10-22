import requests
from requests.auth import HTTPBasicAuth
from requests_ntlm import HttpNtlmAuth
import xmltodict
import json

url = "http://172.70.0.91:8099/api/Query/RMS_CustDepartment_BC?company=2000"

conditions = {
        "Conditions": [
            {
                "DataSourceName": "VYA_CustDeptTable",
                "FieldName": "RecId",
                "Operator": "Equal",
                "Value": "5637146826,5637147593,5637152280"
            }
        ]
    }

data = {
    "startingPosition": 1,
    "numberOfRecordsToFetch": 10,
    "conditions": json.dumps(conditions)
}

res = requests.get(url, auth=HTTPBasicAuth('shruntong\Barcode', 'B.rms123'), params=data, headers={"Content-Type": "text/plain"})
print(res.status_code)
print(res.text)


# 定时同步查询 接口返回结果两种情况
"""
{
  "RMS_QueryService": {
    "VYA_CustDeptTable": [
      {
        "dataAreaId": "1000",
        "VYA_CustDepart": "AGENCY",
        "VYA_CustDepartName": "代理sss"
      },
      {
        "dataAreaId": "1000",

        "VYA_CustDepart": "testbarcode",
        "VYA_CustDepartName": "testbarcode11111"
      }
    ]
  }
}


{
  "RMS_QueryService": {
    "VYA_CustDeptTable": {
      "dataAreaId": "1000",
      "VYA_CustDepart": "AGENCY",
      "VYA_CustDepartName": "代理sss"
    }
  }
}
"""


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
#               <tem:RMS_CustDeptTableServiceFindRequest>
#                  <!--Optional:-->
#                  <quer:QueryCriteria>
#
#                  </quer:QueryCriteria>
#               </tem:RMS_CustDeptTableServiceFindRequest>
#            </soapenv:Body>
#         </soapenv:Envelope>'''
#     headers = [("SOAPAction", "http://tempuri.org/RMS_CustDeptTableService/find"),
#                ("Content-Type", "text/xml;charset=utf-8")]
#     url = "http://172.70.0.49:801/MicrosoftDynamicsAXAif60/RMSCustDepartment/xppservice.svc"
#
#     res = requests.post(url, auth=HttpNtlmAuth('shruntong\Barcode', 'B.rms123'), data=data, headers=dict(headers))
#     print(res.request.headers)
#     print(res.status_code)
#     print(res.text)