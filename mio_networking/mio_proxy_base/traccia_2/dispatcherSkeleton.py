from abc import ABC,abstractmethod
import multiprocess as mp
import sys,socket,time
from dispatcher_service import DispatcherService

def run_function(c,skeleton):
    message = c.recv(1024)

    print(f"messaggio ricevuto :{message.decode('utf-8')}")

    request =message.decode('utf-8').split('-')[0]

    print(f"request: {request}")

    if request == 'sendCmd':
        value_to_send =message.decode('utf-8').split('-')[1]
        print(f"request is sendCmd, value to send: {value_to_send}")
        skeleton.sendCmd(value_to_send)
        result = 'ACK'
    else:
       result = skeleton.getCmd()
       print("request is getCmd, waiting for result\n")
       c.send(result.encode('utf-8'))
       c.close()


        
class DispatcherSkeleton(DispatcherService,ABC):
    def __init__(self,host,port):
        self.port = port
        self.host = host
    @abstractmethod
    def sendCmd(self,value):
        pass

    @abstractmethod
    def getCmd(self):
        pass

    def run_skeleton(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((self.host,self.port))

        self.port = s.getsockname()[1]
        print(f"socket binded to host: {self.host} port: {self.port}")

        s.listen(30)

        while True:

            c,addr =s.accept()
            print(f"connected to : {addr[0]} - {addr[1]}")

            t =mp.Process(target = run_function,args = (c,self))
            t.start()
        s.close()
        print("[DISPATCHER SKELETON] socket is closed\n")
        
