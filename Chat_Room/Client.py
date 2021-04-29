import socket
import threading

def send_message(uname):
    while True:
        message = input('')
        data = uname + ' : ' + message
        client_socket.send(data.encode())

def recieve_message():
    while True:
        data = client_socket.recv(1024).decode()
        print('\n\t\t' + str(data))

if __name__ == '__main__':
    host = socket.gethostname()
    port = 5001
    client_socket = socket.socket()
    uname = input('Enter Your Name in Chat : ')

    client_socket.connect((host,port))
    print('Connected to remote host')

    send_thread = threading.Thread(target=send_message, args=(uname, ))
    send_thread.start()

    recieve_thread = threading.Thread(target=recieve_message, args=())
    recieve_thread.start()
