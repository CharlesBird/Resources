import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_sock(sk, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf8"))
        if data.decode("utf8") == 'exit':
            break
        re_data = input("服务端输入：")
        sock.send(re_data.encode("utf8"))
    sk.close()


while True:
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()
    # data = sock.recv(1024)
    # print(data.decode("utf8"))
    # re_data = input("服务端输入：")
    # # sock.send("Hello {}".format(data.decode("utf8")).encode("utf8"))
    # sock.send(re_data.encode("utf8"))

# sock.close()
# server.close()