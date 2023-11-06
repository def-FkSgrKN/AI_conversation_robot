#TechAcademyマガジン, Pythonでソケット通信を行う方法【初心者向け】,  https://techacademy.jp/magazine/19147, 2022年3月3日.

#サーバー側
import socket

PORT = 50000
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', PORT))
    #s.bind(('192.168.11.49', PORT))
    s.listen()
    while True:
        (connection, client) = s.accept()
        try:
            print('Client connected', client)
            data = connection.recv(BUFFER_SIZE)
            connection.send(data.upper())
        finally:
            connection.close()