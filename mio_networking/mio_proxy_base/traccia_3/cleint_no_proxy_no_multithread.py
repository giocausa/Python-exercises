import random,sys,time,socket

BUFFER_SIZE = 1024

if __name__ == '__main__':
    try:
        HOST = sys.argv[1]
        PORT = sys.argv[2]
    except IndexError:
        print("errore nell inserimento di port e host")
        sys.exit(-1)

    for i in range(10):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((HOST,int(PORT)))

        value_to_deposit = random.randint(0,3)

        request = "sendCmd"
        message_to_send = request + "-" + str(value_to_deposit)

        print("[CLIENT] sending message ",message_to_send)
        time.sleep(2)
        s.send(message_to_send.encode('utf-8'))

        print("[CLIENT] waiting for result...")
        data = s.recv(BUFFER_SIZE)

        print("[CLIENT] data received : "+ data.decode('utf-8'))
        