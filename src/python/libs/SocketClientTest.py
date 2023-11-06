#TechAcademyマガジン, Pythonでソケット通信を行う方法【初心者向け】,  https://techacademy.jp/magazine/19147, 2022年3月3日.

#クライアント側
import socket

PORT = 50000
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', PORT))
    data = input('Please input > ')
    s.send(data.encode())
    print(s.recv(BUFFER_SIZE).decode())