from lxml import etree
import requests
import re
import json

# str_xml = """
# <A xmlns="http://This/is/a/namespace">
#     <B>dataB1</B>
#     <B>dataB2</B>
#     <B>
#         <C>dataC</C>
#     </B>
# </A>
# """
#
# xml = etree.fromstring(str_xml)
# ns = xml.nsmap[None]
# ns = "{%s}" % ns
# for item in xml.findall("{0}B/{0}C".format(ns)): #不能用xpath会出错
#     print(item)

# str_xml = """
# <A xmlns="http://This/is/a/namespace">
#     <B b="123">dataB1</B>
#     <B>dataB2</B>
#     <B>
#         <C>dataC</C>
#     </B>
# </A>
# """
#
# xml = etree.fromstring(str_xml)
# ns = xml.nsmap[None]
# ns = "{%s}" % ns
#
# item = xml.find(ns+"B")
#
# print(item.get('b'))
# print(item.text)

# res = requests.get('http://www.ninghai.gov.cn/col/col111591/index.html')
# html = res.text
html = """<?xml version="1.0"?><root><item><![CDATA[{'name': 123, 'age': 100}]]></item>
<item><![CDATA[{'name': 'CB', 'age': 200}]]></item>
</root>
"""
# print(html)
rgx = re.compile("\<\!\[CDATA\[(.*?)\]\]\>", re.S)
results = re.findall(rgx, html)
for res in results:
    print(res)
    print(type(res))
    res2 = json.loads(res)
    res2['name']
    print(type(res2))
print(results)
