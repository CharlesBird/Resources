import unittest
#

from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor



if __name__ == '__main__':
    url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl'
    # url = 'http://track.tcs.com.pk/trackingaccount/track.asmx?WSDL'
    imp = Import('http://www.w3.org/2001/XMLSchema', location='https://www.w3.org/2001/XMLSchema.dtd')
    imp.filter.add('http://WebXml.com.cn/')
    doctor = ImportDoctor(imp)
    client = Client(url, doctor=doctor)
    print(client)