from threading import Thread,current_thread

class SkeletonThread(Thread):
    def __init__(self,sock,msgClient,addr,thd_name,ref):
        super().__init__(name =self.thd_name)
        self.sock=sock
        self.msgClient=msgClient
        self.addr=addr
        self.ref=ref
    
    def run(self):

        message = self.msgClient.decode("utf-8")

        service=message.split('-')[0]
        articolo = message.split('-')[1]

        result =None

        if service == "preleva":
           result = self.ref.preleva(articolo)
        elif service == "deposita":
            id = message.split('-')[2]
            result = self.ref.deposita(articolo,id)
        else:
            print(f"[{current_thread().name}] Servizio {service} non riconosciuto")
        
        response =str(result)
        self.sock.sendto(response.encode("urf-8"),self.addr)

