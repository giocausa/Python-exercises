import socket,sys,time
from dispatcher_service import DispatcherService
import multiprocess as mp
from abc import ABC,abstractclassmethod

def run(c,skeleton):

    message = c.recv(1024)

    print("[DISPATCHER SKELETON run_function] Messagge received: ",message.decode('utf-8'))

    request = (message.decode('utf-8')).split('-')[0]
    print("[DISPATCHER SKELETON run_function] request received: ",request)

    if request =="sendCmd":
        value_to_send = (message.decode('utf-8')).split('-')[1]
        print("la richiesta è sendCmd, il valore è: ",value_to_send)
        skeleton.sendCmd(value_to_send)
        result ='ACK'
    else:
        print("la richiesta è getCmd, attendi per il result")
        result = skeleton.getCmd()

        print("il risultato da inviare indietro è: ",result)

        c.send(result.encode('utf-8'))
    c.close()

class DispatcherSkeleton(DispatcherService):
    def __init__(self,host,port,dispatcher_service):
        self.host = host
        self.port = port
        self.dispatcher_service = dispatcher_service

    def sendCmd(self,value):
        self.dispatcher_service.sendCmd(value)

    def getCmd(self):
        return self.dispatcher_service.getCmd()
    
    def run_skeleton(self):

        host = 'localhost'

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((self.host,self.port))
        self.port= s.getsockname()[1]

        print("socket collegata all host: "+self.host+" PORT:"+str(self.port))

        s.listen(30)
    
        while True:
            c,addr =s.accept()
            print("connect to :",addr[0],"-",addr[1])

            t = mp.Process(target = run,args = (c,self))
            t.start()
        s.close()
    