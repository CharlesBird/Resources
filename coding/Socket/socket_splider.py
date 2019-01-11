import websocket
# wss://stream11.forexpros.com/echo/146/6pazbm4h/websocket
# wss://stream265.forexpros.com/echo/938/9rohh63z/websocket
# wss://stream138.forexpros.com/echo/072/7w51txmq/websocket
# wss://stream196.forexpros.com/echo/613/l2iw9i00/websocket
# wss://stream341.forexpros.com/echo/282/uts5r6id/websocket
ws = websocket.create_connection('wss://stream138.forexpros.com/echo/072/7w51txmq/websocket', timeout=10)

# {"_event":"bulk-subscribe","tzID":28,"message":"pid-8833:%%pid-44634:%%pid-985364:%%pid-40820:%%pid-28930:%%pid-179:%%pid-942630:%%pid-8873:%%pid-8839:%%pid-8827:%%pid-1055949:%%pid-1:%%pid-2:%%pid-3:%%pid-5:%%pid-7:%%pid-9:%%pid-10:%%pidTechSumm-1:%%pidTechSumm-2:%%pidTechSumm-3:%%pidTechSumm-5:%%pidTechSumm-7:%%pidTechSumm-9:%%pidTechSumm-10:%%pidExt-8833:%%isOpenExch-1:%%isOpenExch-97:%%isOpenExch-54:%%isOpenExch-21:%%isOpenExch-103:%%isOpenExch-1004:%%isOpenPair-8833:%%isOpenPair-8873:%%isOpenPair-8839:%%isOpenPair-8827:%%cmt-6-5-8833:%%domain-6:"}
# {"_event":"bulk-subscribe","tzID":28,"message":"pid-40820:%%pid-100634:%%pid-100541:%%pid-942827:%%pid-100933:%%pid-100448:%%pid-996084:%%pid-100736:%%pid-100907:%%pid-953917:%%pid-102952:%%pid-100468:%%pid-101094:%%pid-100425:%%pid-100530:%%pid-100883:%%pid-28930:%%pid-179:%%pid-942630:%%pid-8873:%%pid-8839:%%pid-8827:%%pid-1055949:%%pid-1:%%pid-2:%%pid-3:%%pid-5:%%pid-7:%%pid-9:%%pid-10:%%pid-8833:%%pidTechSumm-1:%%pidTechSumm-2:%%pidTechSumm-3:%%pidTechSumm-5:%%pidTechSumm-7:%%pidTechSumm-9:%%pidTechSumm-10:%%pidExt-40820:%%isOpenExch-54:%%isOpenExch-21:%%isOpenExch-103:%%isOpenExch-1004:%%isOpenPair-8873:%%isOpenPair-8839:%%isOpenPair-8827:%%cmt-6-5-40820:%%domain-6:"}
# ws.send('[{"_event":"bulk-subscribe","tzID":28,"message":"pid-40820"}]')
ws.send('[{"_event":"UID","UID":0}]')
data = ws.recv()
print(data)