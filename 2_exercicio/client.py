import socket

server = socket.gethostbyname(socket.gethostname())
port = 2200
encoding_format = 'utf-8'
size = 1024

def client():
    #Create socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server,port))

    #Open file with read mode.
    file = open(input("Arquivo: "),"r")
    data = file.read()

    #Sent filename
    client.send("arquivo.txt".encode(encoding_format))
    msg = client.recv(size).decode(encoding_format)
    print(f"[SERVER]: {msg}")

    #Sent file
    client.send(data.encode(encoding_format))
    msg = client.recv(size).decode(encoding_format)
    print(f"[SERVER]: {msg}")

    file.close()
    client.close()

client()