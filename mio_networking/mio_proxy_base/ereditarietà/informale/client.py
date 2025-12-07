from Interface import Subject
import socket,sys

class Proxy(Subject):
    def __init__(self,port):
        self.port=port
    
    def request(self,message):

        IP = 'localhost'
        BUFFER_SIZE = 1024

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((IP,self.port))

        s.send(message.encode('utf-8'))

        data =s.recv(BUFFER_SIZE)

        print("data ricevuto: "+data.decode('utf-8'))
        s.close()

if __name__ == '__main__':
    try:
        PORT = sys.argv[1]
        MESSAGE = sys.argv[2]
    except IndexError:
        print("port inserita errata imbecille")
        sys.exit(1)
    print("[Client] genereting request on port: ",PORT," Message: ",MESSAGE)
    proxy = Proxy(int(PORT))
    proxy.request(MESSAGE)