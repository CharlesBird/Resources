import requests
import json

class YunPian(object):
    """
    云片平台短信接口
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, code, mobile):
        """
        发送短信
        :param code:
        :param mobile:
        :return:
        """
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【张怀成】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == '__main__':
    yunpan = YunPian("7cf8e841f59cd34184abacb6c4b2d444")
    yunpan.send_sms('1234', '13585671186')
