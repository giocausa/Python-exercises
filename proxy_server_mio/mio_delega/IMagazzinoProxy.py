from IMagazzino import IMagazzino
import socket

class IMagazzinoProxy(IMagazzino):
    def __init__(self,ip,port):
        self.port =port
        self.ip = ip
        self.buf_size = 1024

        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    
    def deposita(self,articolo,id):
        message_to_send = '-'.join(["deposita",articolo,str(id)])
        print("[MAGAZZINO PROXY] richiesta inviata :",message_to_send)


        self.sock.sendto(message_to_send.encode("utf-8"),(self.ip,self.port))
        response, addr =self.sock.recvfrom(self.buf_size)

        print("[MAGAZZINO PROXY]risposta: ",response.decode("utf-8"))

        return bool(response)
    
    def preleva(self,articolo):
        message_to_send ='-'.join("preleva",articolo)
        print("[MAGAZZINO PROXY] richiesta inviata :",message_to_send)

        self.sock.sendto(message_to_send.encode("utf-8"),(self.ip,self.port))
        response, addr =self.sock.recvfrom(self.buf_size)

        response_message = response.decode("utf-8")
        print("[MAGAZZINO PROXY]risposta: ",response_message)
        return int(response_message)



