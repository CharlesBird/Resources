# 行不通，异步验证方式没有HttpNtlmAuth
import requests
from requests_ntlm import HttpNtlmAuth
import asyncio
import aiohttp


async def fetch(session):
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
                  <tem:RMS_InventSiteServiceFindRequest>
                     <!--Optional:-->
                     <quer:QueryCriteria>

                     </quer:QueryCriteria>
                  </tem:RMS_InventSiteServiceFindRequest>
               </soapenv:Body>
            </soapenv:Envelope>'''
    headers = [("SOAPAction", "http://tempuri.org/RMS_InventSiteService/find"),
               ("Content-Type", "text/xml;charset=utf-8")]
    url = "http://172.70.0.49:801/MicrosoftDynamicsAXAif60/RMSInventSite/xppservice.svc"

    async with session.post(url, data=data, headers=dict(headers)) as resp:
        print('url status: {}'.format(resp.status))
        if resp.status in (200, 201):
            data = await resp.text()
            return data
    return data

async def main(loop):

    async with aiohttp.ClientSession(auth=aiohttp.BasicAuth('shruntong\Barcode', 'B.rms123'), loop=loop) as session:
        res = await fetch(session)
        print(res)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    # asyncio.ensure_future(main())
    # loop.run_forever()