from pyquery import PyQuery as pq

html = '''<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul></div>'''
"""
http://www.pythonsite.com/?p=185
初始化的时候一般有三种传入方式：传入字符串，传入url,传入文件
"""
doc = pq(html)
# print(doc)
# print(type(doc))
# print(doc('li'))
print(doc('#container .list li'))
print(doc('.list'))