import requests
url = 'http://hq.sinajs.cn/list=hf_OIL,hf_CL,hf_CAD,hf_S'

response = requests.get(url)
print(response.text)