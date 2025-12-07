import socket,sys

def Client(port):
    IP ="localhost"
    BUFF_SIZE=1024
    MESSAGE= "Francesco Totti 10"

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((IP,port))
    s.send(MESSAGE.encode('utf-8'))


    data = s.recv(BUFF_SIZE)

    print("messaggio ricevuto : "+ data.decode('utf-8'))

    s.close()

if __name__ == '__main__':
    try:
        port = sys.argv[1]
    except IndexError:
        print("errore nel port selezionato")
        sys.exit(1)

    assert port != "","specifica la porta"
    Client(int(port))
