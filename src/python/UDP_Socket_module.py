from socket import socket, AF_INET, SOCK_DGRAM


def make_server_socket(HOST="127.0.0.1", PORT=5000):
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind((HOST, PORT))

    return server_socket


def make_client_socket(ADDRESS="127.0.0.1", PORT=5001):
    client_socket = socket(AF_INET, SOCK_DGRAM)

    return client_socket


def socket_receve_data(made_socket, MESSAGE_SIZE=8192):
    byte_msg, address = made_socket.recvfrom(MESSAGE_SIZE)
    msg = byte_msg.decode('utf-8')

    return msg, address


def socket_send_data(made_socket, msg, ADDRESS, PORT):
    made_socket.sendto(msg.encode(), (ADDRESS, PORT))


def close_socket(made_socket):
    made_socket.close()



def socket_server_test_use():

    HOST = "127.0.0.1"
    PORT = 5000
    
    server_socket = make_server_socket(HOST, PORT)
    print("socket_made")


    MESSAGE_SIZE = 8192

    while True:
        msg, address = socket_receve_data(server_socket ,MESSAGE_SIZE)
        print(f"message: {msg}\nfrom: {address}")

        if msg == "[EXCEPTION]_END":
            break
        

    close_socket(server_socket)



def socket_client_test_use():
    PORT = 5001
    ADDRESS = "127.0.0.1" # 自分に送信

    client_socket = make_client_socket(ADDRESS, PORT)

    print("client_made")

    while True:
        msg = input("> ")
        # 送信
        socket_send_data(client_socket, msg, ADDRESS, PORT)

        if msg == "[EXCEPTION]_END":
            break

    close_socket(client_socket)





"""
HOST = "127.0.0.1"
PORT = 5000

# ソケットを用意
#print("AF_INET=" + str(AF_INET))
#print("SOCK_DGRAM=" + str(SOCK_DGRAM))
s = socket(AF_INET, SOCK_DGRAM)
# バインドしておく
s.bind((HOST, PORT))

while True:
    # 受信
    byte_msg, address = s.recvfrom(8192)
    msg = byte_msg.decode('utf-8')

    print(f"message: {msg}\nfrom: {address}")

    if msg == "[EXCEPTION]_END":
        break

# ソケットを閉じておく
s.close()
"""



"""
PORT = 5000
ADDRESS = "127.0.0.1" # 自分に送信

s = socket(AF_INET, SOCK_DGRAM)
# ブロードキャストする場合は、ADDRESSを
# ブロードキャスト用に設定して、以下のコメントを外す
# s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    msg = input("> ")
    # 送信
    s.sendto(msg.encode(), (ADDRESS, PORT))

    if msg == "[EXCEPTION]_END":
        break

s.close()
"""


if __name__ == "__main__":
    socket_server_test_use()