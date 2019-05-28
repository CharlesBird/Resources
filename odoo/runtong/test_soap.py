import SOAPpy, base64

class myHTTPTransport(SOAPpy.HTTPTransport):
    username = None
    passwd = None

    @classmethod
    def setAuthentication(cls,u,p):
        cls.username = u
        cls.passwd = p

    def call(self, addr, data, namespace, soapaction=None, encoding=None, http_proxy=None, config=SOAPpy.Config, timeout=None):

        if not isinstance(addr, SOAPpy.SOAPAddress):
          addr = SOAPpy.SOAPAddress(addr, config)

        if self.username != None:
          addr.user = self.username+":"+self.passwd

        return SOAPpy.HTTPTransport.call(self, addr, data, namespace, soapaction, encoding, http_proxy, config)


if __name__ == '__main__':

  # code for authenticating the SOAP API calls
  myHTTPTransport.setAuthentication('shruntong\Barcode', 'B.rms123')

  Baton = SOAPpy.WSDL.Proxy('http://172.70.0.49:801/MicrosoftDynamicsAXAif60/test5/xppservice.svc?wsdl', transport=myHTTPTransport)