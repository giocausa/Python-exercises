import socket,sys,time,random
from dispatcher_service import DispatcherService

BUFFER_SIZE = 1024

class DispatcherProxy(DispatcherService):
    def __init__(self,host,port,name,request_number):
        self.host = host
        self.port = port
        self.name = name
        self.request_number = request_number
    
    def sendCmd(self,value):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.host,int(self.port)))

        request ="sendCmd"

        message_to_send = request + "-"+ str(value)
        
        print(f"[CLIENT THREAD NAME : {self.name}] using sock ref: {hex(id(s))}")
        print(f"[CLIENT THREAD NAME: {self.name}]\t\t\Sending: #{self.request_number} message: {message_to_send}\n")

        time.sleep(random.randint(2,4))
        s.send(message_to_send.encode('utf-8'))

        print(f"[CLIENT THREAD NAME: {self.name}],\t\t\t waiting for result for #{self.request_number} request\n")

        data = s.recv(BUFFER_SIZE).decode('utf-8')
        print(f"[CLIENT THREAD NAME: {self.name}] \t\t\t data received: {data:s} for #{self.request_number} request\n")

        s.close()
    
    def getCmd(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.host,int(self.port)))

        message_to_send ="getCmd"

        print(f"[ACTUATOR] sending #{self.request_number} request: {message_to_send}\n")
        time.sleep(1)
        s.send(message_to_send.encode('utf-8'))

        print(f"[ACTUATOR] waiting result for #{self.request_number} request\n")
        data = s.recv(BUFFER_SIZE).decode('utf-8')

        return data
        
        
