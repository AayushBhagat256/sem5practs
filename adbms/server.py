import socket

def server():
    host = "127.0.0.1"
    port = 7000
    msg = "PREPARE"
    log = msg
    over = 0

    con_soc = socket.socket()
    con_soc.bind((host, port))
    con_soc.listen(2)

    while not over:
        replies = []
        for i in range(3):
            conn, add = con_soc.accept()
            conn.send(msg.encode())
            data = conn.recv(1024).decode()
            replies.append(data.upper())
            print(f'The subordinator msg is {data.upper()}')
            conn.close()

        if over == 1:
            break

        if "ABORT" in replies or len(replies) < 3:
            msg = "ABORT"
            print("TRANSACTION ABORTED!\nThe final log is: ", log + " " + msg)
            over = 1
        elif "SUCCESS" in replies:
            msg = "SUCCESS"
            print("TRANSACTION SUCCESS!\nThe final log is: ", log + " " + msg)
            over = 1
        else:
            msg = "PREPARE TO COMMIT"

        log = log + ' ' + msg

    con_soc.close()

server()
