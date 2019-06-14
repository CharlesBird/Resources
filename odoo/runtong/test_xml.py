from lxml import etree

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

str_xml = """
<A xmlns="http://This/is/a/namespace">
    <B b="123">dataB1</B>
    <B>dataB2</B>
    <B>
        <C>dataC</C>
    </B>
</A>
"""

xml = etree.fromstring(str_xml)
ns = xml.nsmap[None]
ns = "{%s}" % ns

item = xml.find(ns+"B")

print(item.get('b'))
print(item.text)