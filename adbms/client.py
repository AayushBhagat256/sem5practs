import socket

def client():
    host = "127.0.0.1"
    port = 7000
    log = ''
    over = 0
    try:
        conn_soc = socket.socket()
        conn_soc.connect((host, port))

        while not over:
            revdata = conn_soc.recv(1024).decode()
            print(f'The received data is: {revdata.upper()}')

            if revdata.upper() == "ABORT" or revdata.upper() == "SUCCESS":
                msg = "OK"
                over = 1
                print(f"TRANSACTION {revdata.upper()}!")
            else:
                msg = input("System Status: ").upper()
                log += " " + msg

            conn_soc.send(msg.encode())

        conn_soc.close()
    except Exception as e:
        print("Exception:", e)

client()
