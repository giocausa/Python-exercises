import socket,sys,time

def Client(port):
    msgClient = "ciao Mimmo\n"
    buff_size = 1024
    serveraddressport = ("localhost",port)

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    print("[Client] invio dati al server: ",msgClient)

    start_time=time.time()
    s.sendto(msgClient.encode('utf-8'),serveraddressport)

    msgServer, addr =s.recvfrom(buff_size)
    end_time=time.time()

    latenza = (end_time-start_time)*1000

    print("[Client] Risposta del server: ",msgServer.decode('utf-8'))
    print(f"[Client] latenza : {latenza:.3f} ms")
    s.close()

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except(IndexError,ValueError):
        print("errore nell inserimento del PORT")
        sys.exit(1)
    
Client(port)
