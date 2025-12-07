import socket,sys,random,time
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

        request = "sendCmd"
        message_to_send= request + "-" + str(value)
        print(f"[CLIENT Thread name: {self.name}] using socket ref: {hex(id(s))}")
        print(f"[CLIENT Thread name: {self.name}]\t\t\t Sending: {message_to_send}\n")
        time.sleep(random.randint(2,4))
        s.send (message_to_send.encode('utf-8'))

        data = s.recv(BUFFER_SIZE).decode('utf-8')
        print(f'[CLIENT Thread name: {self.name}] \t\t\tdata received: {data:s} for #{self.request_number} request\n')
        s.close()

    def getCmd(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        s.connect((self.host,int(self.port)))

        message = "getCmd"
        print(f"[ACTUATOR] message to send for request number #{self.request_number} message : {message}\n")
        time.sleep(random.randint(2,4))

        s.send(message.encode('utf-8'))
        print(f"receive data for request: {self.request_number} waiting\n")
        data = s.recv(BUFFER_SIZE).decode('utf-8')
        s.close()
        return data
     