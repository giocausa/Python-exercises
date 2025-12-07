import socket,sys,time

IP = 'localhost'

def Client(PORT,s):
    BUFFER_SIZE = 1024
    MESSAGE ="nun ma fa vre a cart caroo\n"

    start_time = time.time()
    s.send(MESSAGE.encode('utf-8'))

    data =s.recv(BUFFER_SIZE)
    end_time=time.time()

    latenza=(end_time-start_time)*1000

    print(f"messaggio ricevuto: {data.decode('utf-8')}")
    print(f"latenza: {latenza:.3f} ms")


if __name__ == '__main__':
    try:
        PORT = int(sys.argv[1])
    except (IndexError,ValueError):
        print("errore inserimento porta")
        sys.exit(1)

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((IP,PORT))

    while True:
        Client(PORT,s)
        time.sleep(1)


