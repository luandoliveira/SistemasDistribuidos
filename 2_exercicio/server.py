import socket
import os

ip_server = socket.gethostbyname(socket.gethostname())
port = 2200
encoding_format = 'utf-8'
size = 1024
path = r"recv"
file_name = r"recebido.txt"

def server():
    print("[CRITICAL] Starting server.")
    #Create socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip_server,port))
    print("[CRITICAL] Sever is listening.")
    server.listen()

    while True:
        conn, addr = server.accept()
        print(f"[INFO] Connection with {addr[0]} on port {addr[1]} has been established.")
        conn.send("[INFO] Welcome to the server.".encode(encoding_format))

        #Receive filename
        filename = conn.recv(size).decode(encoding_format)
        print("[INFO] Filename received.")

        #Check if dir has been existing, if false create the directory
        if os.path.isdir(path) is False: os.makedirs(r"./recv")

        #Receive file
        file = open(r"recv/"+filename,"w")
        conn.send("File received.".encode(encoding_format))

        data = conn.recv(size).decode(encoding_format)
        print(f"[RECV] File data received.")
        file.write(data)
        conn.send("File data recv.".encode(encoding_format))


        file.close()
        conn.close()
        print(f"[INFO] {addr} has been disconnected.")

        #Rename file for filename inserted on the code
        try:
            if os.path.isfile(r"recv/arquivo.txt"):
                os.rename(r"recv/arquivo.txt",f"{path}/{file_name}")
        except FileExistsError:
            os.remove(f"{path}/{file_name}")
        finally:
            if os.path.isfile(r"recv/arquivo.txt"):
                os.rename(r"recv/arquivo.txt",f"{path}/{file_name}")

server()