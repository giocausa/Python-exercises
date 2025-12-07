import socket

IP ="0.0.0.0"
PORT = 0
BUFFER_SIZE = 1024

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((IP,PORT))
s.listen(1) #si mette in ascolto con max 1 client

cur_port = s.getsockname()[1]#restituisce la porta su cui sono collegato

print("server: ",IP," Port: ", cur_port)

while True:
    conn, addr =s.accept()#aspetta ceh qualcuno si collegs 
    print("client addr: "+str(addr))
    print('Connection addr: {}'.format(addr))
    toClient= "SEMPE FOZZA NAPULE\n"

    data = conn.recv(BUFFER_SIZE)
    print("received data: "+data.decode("utf-8"))


    conn.send(toClient.encode("utf-8"))
    conn.close()

s.close()
