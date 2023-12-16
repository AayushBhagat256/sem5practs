import socket 

def server():
    port = 8000
    host = "127.0.0.1"
    print('Server is running')
    soc = socket.socket()
    soc.bind((host, port))
    soc.listen(2)

    while True:
        conn, addr = soc.accept()
        print(f'Connection from {addr}')

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break  # Exit the loop if no data is received
            print(f'Client ({addr}): {data}')
            conn.send("Message received".encode())

        conn.close()
        print(f'Connection with {addr} closed')

server()
