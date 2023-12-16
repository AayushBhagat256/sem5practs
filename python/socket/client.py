import socket

def client():
    print("Client side : ")
    port = 8000
    host = "127.0.0.1"
    soc = socket.socket()
    soc.connect((host, port))
    
    while True:
        msg = input("Enter your msg : ")
        soc.send(msg.encode())
        
        data = soc.recv(1024).decode()
        print(f'Server : {data}')

client()
