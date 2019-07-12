import requests
from requests_ntlm import HttpNtlmAuth
import re
import xmltodict
import json


if __name__ == '__main__':
    data = '''
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:dat="http://schemas.microsoft.com/dynamics/2010/01/datacontracts" xmlns:arr="http://schemas.microsoft.com/2003/10/Serialization/Arrays" xmlns:tem="http://tempuri.org">
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
              <tem:RMS_InventoryOnhandServiceGetInventoryDataRequest>
                 <!--Optional:-->
                 <tem:_jsonParameter><![CDATA[{
            JsonParameters:{
            1: {
            ItemId: '10001000001',    
            InventSiteId:'' ,
            InventLocationId:'',
            WMSLocationId:'',
            InventBatchId:'' ,
            CurrentPageNo: '1',
            PageSize: '5'
            },
            2: {
            ItemId: 'b',
            InventSiteId:'McLaughlin' ,
            InventLocationId:'McLaughlin',
            WMSLocationId:'McLaughlin',
            InventBatchId:'McLaughlin',
            CurrentPageNo: '1',
            PageSize: '5'
            }
            }
            }]]></tem:_jsonParameter>
              </tem:RMS_InventoryOnhandServiceGetInventoryDataRequest>
           </soapenv:Body>
        </soapenv:Envelope>'''
    headers = [("SOAPAction", "http://tempuri.org/RMS_InventoryOnhandService/getInventoryData"),
               ("Content-Type", "text/xml;charset=utf-8")]
    url = "http://172.70.0.49:801/MicrosoftDynamicsAXAif60/RMSInventoryOnhandService/xppservice.svc"

    res = requests.post(url, auth=HttpNtlmAuth('shruntong\Barcode', 'B.rms123'), data=data, headers=dict(headers))
    print(res.request.headers)
    print(res.status_code)
    # print(res.text)
    html = res.text
    # print(html)
    # html2 = re.sub(r'&#xD;', '', html, flags=re.I)
    # print(html2)
    rgx = re.compile("\!\[CDATA\[(.*?)\]\]", re.S)
    results = re.findall(rgx, html)
    for r in results:
        print(r)
        json_res = json.loads(r)
        print(json_res)
        print(json_res['Response'])
