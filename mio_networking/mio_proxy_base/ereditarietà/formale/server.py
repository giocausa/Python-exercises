from abc import ABC,abstractmethod
from Interface import Subject
import socket,sys
import threading

def thd_fun(self,c):

    data = c.recv(5000)

    result =self.request(data)

    c.send(result)

    c.close()


class Skeleton(Subject,ABC):
    def __init__(self,port):
        self.port=port
    @abstractmethod
    def request(self,data):
        pass

    def run_skeleton(self):
        host ='localhost'

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((host,self.port))

        self.port = s.getsockname()[1]

        print("socket connected to port",self.port)

        s.listen()

        while True:

            c,addr =s.accept()
            print("Connected to: "+addr[0],"-",addr[1])

            t = threading.Thread(target=thd_fun,args=(self,c),)
            t.start()
        s.close()

class RealSubject(Skeleton):
    def request(self,data):

        data = data[::-1]

        return data

if __name__ == '__main__':
    try:
        PORT =sys.argv[1]
        
    except IndexError:
        print("please insert correct PORT argv")
        sys.exit(1)
    
    realsubject = RealSubject(int(PORT))

    realsubject.run_skeleton()

