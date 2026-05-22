import threading
import socket



server_port=9000
server_host='127.0.0.1'


def handle_msg(conn):
    while True:
        data = conn.recv(1024)
        msg = data.decode('utf-8')
        print(f'Chegou {msg}\n')


if __name__ == '__main__':
    cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cliente.connect((server_host,server_port))

    t = threading.Thread(target=handle_msg,args=(cliente,),daemon=1)
    t.start()

    try:
        while True:
            msg = input()
            cliente.send(msg.encode('utf-8'))
    finally:
        cliente.close()






