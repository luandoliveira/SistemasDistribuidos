import socket
import threading

server = '192.168.116.1'
port = 8080
encoding_format = 'utf-8'

#Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server,port))

#Send the name of the author of the message.
def send_name():
    name = str(input("Say your name: "))
    to_send("name=" + name)

#Send the author's message
def send_message():
    while True:
        message = str(input())
        to_send("msg=" + message)

#Send message
def to_send(message):
    client.send(message.encode(encoding_format))

#Start sending name and message
def start_send():
    send_name()
    send_message()

#Handle_mensagens and displayed
def handle_mensagens():
    while(True):
        msg = client.recv(1024).decode()
        split_msg = msg.split("=")
        print(f"{split_msg[1]} : {split_msg[2]}")

def start():
    thread_1 = threading.Thread(target=handle_mensagens)
    thread_2 = threading.Thread(target=start_send)
    thread_1.start()
    thread_2.start()

start()