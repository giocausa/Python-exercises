import socket,sys

def client(PORT):
    IP ='localhost'
    BUFF_SIZE = 1024
    MESSAGE = "el matador"

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((IP,PORT))#stabilisce la connesssione

    s.send(MESSAGE.encode('utf-8'))#invio messaggio trasformandolo in byte

    data = s.recv(BUFF_SIZE)#ricezione messaggio

    print("risposta del server: "+data.decode('utf-8'))


    s.close()

if __name__ =='__main__':
    try:
        PORT = sys.argv[1]
    except IndexError:
        print("errore nell inserimento della port")
        sys.exit(1)
    assert PORT != "",'specifica la port'
    client(int(PORT))

