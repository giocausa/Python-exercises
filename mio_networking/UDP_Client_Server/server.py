import socket

MSGserver = "Ciao Toto"
addressport=("localhost",0)
BUFF_SIZE=1024

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(addressport)

cur_port=s.getsockname()[1]

print("PORT: ",cur_port)

while True:
    MSGClient, addr =s.recvfrom(BUFF_SIZE)
    print("Messaggio dal client ricevuto :"+MSGClient.decode('utf-8'))
    print("address connessione: ".format(addr))

    print("[server] invio messaggio al client")
    s.sendto(MSGserver.encode('utf-8'),addr)
