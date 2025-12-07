import socket
import sys
import time

def client(PORT):
    IP = 'localhost'
    BUFFER_SIZE = 1024
    MESSAGE = "E vabbe, Forza Napule\n"

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((IP,PORT))

    start_time =time.time()

    s.send(MESSAGE.encode('utf-8'))

    data =s.recv((BUFFER_SIZE))
    end_time =time.time()

    latenza = (start_time-end_time)*1000

    print(f"message received:{data.decode('utf-8')}")
    print(f"Round-trip latency: {latenza:.3f}ms")

if __name__== "__main__":
    try:
        PORT = int(sys.argv[1])
    except(IndexError,ValueError):
        print("specifica una port valida")
        sys.exit(1)
        
    while True:
        client(PORT)
        time.sleep(1)

