import threading
import socket



server_port=9000
server_host='127.0.0.1'
lock = threading.Lock()
list_conn = []

def send_all(data, conn):
    with lock:
        for c in list_conn:
            if c != conn:
                c.send(data)

def handle_client(conn, addr):
    while True:
        data = conn.recv(1024)
        msg = data.decode('utf-8') + '=>' +  str(addr[0]) +':' + str(addr[1]) 
        print(f'Mensagem chegou no servidor {msg} do {addr}')
        send_all(msg.encode('utf-8'), conn)


if __name__ == '__main__':
    servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    servidor.bind((server_host,server_port))
    servidor.listen()

    try:
        while True:
            conn, addr = servidor.accept()
            with lock:
                list_conn.append(conn)
            t = threading.Thread(target=handle_client,args=(conn,addr,),daemon=True)
            t.start()
    finally:
        servidor.close()






