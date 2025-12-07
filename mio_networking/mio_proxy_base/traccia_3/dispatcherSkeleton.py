import socket,sys,time
from abc import ABC,abstractmethod
from dispatcher_service import DispatcherService
import multiprocess as mp 

def run_function(c,skeleton):
    message = c.recv(1024)

    print(f"messaggio ricevuto: {message.decode('utf-8')}")

    request = (message.decode('utf-8')).split('-')[0]
    print(f"[DISPATCHERSkeleton] request received: {request}")

    if request == 'sendCmd':
        value_to_send =(message.decode('utf-8')).split('-')[1]
        print(f"[DispatcherSkeleton] request is SendCmd, value is : {value_to_send} ")

        skeleton.sendCmd(value_to_send)
        result = "ACK"
    else:
        print("[DispatcherSkeleton] request is getCmd, wait for result\n")
        result = skeleton.getCmd()

    print(f"[DispatcherSkeleton] result come back is : {result}")

    c.send(result.encode('utf-8'))

    c.close()


class DispatcherSkeleton(DispatcherService,ABC):
    def __init__(self,host,port):
        self.host = host
        self.port = port
        
    @abstractmethod
    def sendCmd(self,value):
        pass

    @abstractmethod
    def getCmd(self):
        pass

    def run_skeleton(self):
        host = 'localhost'

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((self.host,self.port))
        self.port = s.getsockname()[1]

        print("socket binded to host: "+self.host+" "+ str(self.port))

        s.listen(30)

        while True:
            c,addr =s.accept()
            print("connected to : ",addr[0],"-",addr[1])

            t =mp.Process(target = run_function,args = (c,self))
            t.start()
            print("[DispatcherSkeleton] thread is terminated")
            
        s.close()
        print("[DispatcherSkeletoon] socket is closed...")
            