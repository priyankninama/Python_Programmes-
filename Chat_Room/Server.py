import socket
import threading
import time

def accept_client():
    while True:
        conn, addr = server_socket.accept()
        CONNECTION_LIST.append(conn)
        client_thread = threading.Thread(target=broadcast_user, args=(conn, ))
        client_thread.start()

def broadcast_user(cli_socket):
    while True:
        try:
            data = cli_socket.recv(1024).decode()
            if data:
                broadcast_message_client(cli_socket, data)
        except Exception as x:
            print(x.message)
            break

def broadcast_message_client(cli_socket, message):
    for client in CONNECTION_LIST:
        if client != cli_socket:
            client.send(message.encode())

if __name__ == '__main__':
    CONNECTION_LIST = []
    host = socket.gethostname()
    port = 5001
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)
    print('Chat Room Started on port %d' % (port))
    server_thread = threading.Thread(target=accept_client, args=())
    server_thread.start()

