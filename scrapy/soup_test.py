from bs4 import BeautifulSoup
import re

html = '''<html><head><title>The Dormouse's story</title></head><body>
<p class="title"><b>The Dormouse's story</b></p><p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;and they lived at the bottom of a well.</p>
<p class="story">...</p>'''
soup = BeautifulSoup(html,'lxml')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p["class"])
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find(id='link3'))
# for link in soup.find_all('a'):
#     print(link.get('href'))
#     print(soup.get_text())

# print(type(soup.a))
# print(soup.name)
# print(soup.p.attrs)
# print(soup.p['class'])
# print(soup.p.string)
# print(type(soup.a.string))
# print(soup.head.contents)

# for child in soup.body.children:
#     """子节点"""
#     print(child)

# for child in soup.body.descendants:
#     """子孙节点"""
#     print(child)

# for str in soup.strings:
#     """获取多个内容"""
#     print(repr(str))

# for str in soup.stripped_strings:
#     """输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容"""
#     print(repr(str))

# """父节点"""
# print(soup.p.parent.name)
#
# for par in soup.head.title.string.parents:
#     """全部父节点"""
#     print(par.name)

"""
find_all( name , attrs , recursive , text , **kwargs )
find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
"""
print(soup.find_all('b'))
for t in soup.find_all(re.compile("^b")):
    print(t.name)
print(soup.find_all(["a", "b"]))
for t in soup.find_all(True):
    print(t.name)