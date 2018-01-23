import requests
from fake_useragent import UserAgent
s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/123456")
response = s.get("http://httpbin.org/cookies")
print(response.text)
# ua = UserAgent()
# h = ua.random
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"}
# res = requests.get('https://www.zhihu.com', headers=headers)
# print(res.text)
