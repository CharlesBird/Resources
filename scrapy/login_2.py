import requests
from bs4 import BeautifulSoup

Base_URL = "http://192.168.3.50:8069/web"
Login_URL = "http://192.168.3.50:8069/web/login"

def get_odoo_html(url):
    response = requests.get(url)
    first_cookie = response.cookies.get_dict()
    return response.text, first_cookie



def get_token(html):
    soup = BeautifulSoup(html, 'lxml')
    res = soup.find("input", attrs={"name": "csrf_token"})
    token = res["value"]
    return token


def odoo_login(url, token, cookie):
    data = {
        "csrf_token": token,
        "login": "admin",
        "password": "1",
        'redirect': ''
    }
    response = requests.post(url, data=data, cookies=cookie)
    print(response.status_code)
    cookie = response.cookies.get_dict()
    return cookie


if __name__ == '__main__':
    html, cookie = get_odoo_html(Base_URL)
    token = get_token(html)
    cookie = odoo_login(Login_URL, token, cookie)
    response = requests.get("http://192.168.3.50:8069/web#view_type=list&model=manage.issue&menu_id=244&action=331", cookies=cookie)
    print(response.text)