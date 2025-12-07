import socket

IP ='0.0.0.0'
PORT = 0
BUFFER_SIZE =1024

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((IP,PORT))
s.listen(1)

cur_port = s.getsockname()[1]

print("PORT: ",cur_port," IP: ",IP)

while True:
    conn, addr=s.accept()
    print("Client: "+str(addr))
    print(" indirizzo Connessione: {}".format(addr))
    toClient = "DOM PAR O CAZZ\n"


    try:
        while True:
            data =conn.recv(BUFFER_SIZE)
            if not data:
                print("no DATA,connection close")
                break
            print("received data: "+data.decode("utf-8"))
            conn.send(toClient.encode("utf-8"))
    except ConnectionResetError:
        print("errore nella connessione")
    finally:
        conn.close()
s.close()


