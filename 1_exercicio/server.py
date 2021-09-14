import time
import socket
import threading


#DEFININDO SERVIDOR
ip_server = socket.gethostbyname(socket.gethostname())
port = 8080
encoding_format = 'utf-8'

#Criando socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_server,port))

connections, messages = [], []

#Mensagens
def handle_clientes(conn, addr):
    print(f"[INFO] New user are connected with ip address: {addr}")
    global connections,messages
    name = False

    while(True):
        msg = conn.recv(1024).decode(encoding_format)
        if(msg):
            if(msg.startswith("name=")):
                split_msg = msg.split("=")
                name = split_msg[1]
                map_connection = {
                    "conn": conn,
                    "addr": addr,
                    "name": name,
                    "last": 0
                }
                connections.append(map_connection)
                send_individual_user(map_connection)
            elif(msg.startswith("msg=")):
                split_msg = msg.split("=")
                message = name + "=" + split_msg[1][::-1]
                messages.append(message)
                send_message_all_users()

#Enviar mensagem individual
def send_individual_user(connection):
    print(f"[INFO] Sending message for {connection['addr']}")
    for i in range(connection['last'], len(messages)):
        message = "msg=" + messages[i]
        connection['conn'].send(message.encode())
        connection['last'] = i + 1
        time.sleep(0.2)

#Enivar mensagem para todos
def send_message_all_users():
    global connections
    for connection in connections:
        send_individual_user(connection)


def start():
    print(f"[INFO] Starting socket with ip addres {ip_server}:{port}")
    server.listen()
    while(True):
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clientes, args=(conn, addr))
        thread.start()

start()
