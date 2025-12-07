from IMagazzino import IMagazzino
from SkeletonThread import SkeletonThread

class IMagazzinoSkeleton(IMagazzino):
    def __init__(self,port,ip,delegate):
        self.port=port
        self.ip=ip
        self.buf_size =1024
        self.delegate=delegate

    def deposita(self,articolo,id):
        return self.delegate.deposita(articolo,id)

    def preleva(self,articolo):
        return self.delegate.preleva(id)

    
    def runSkeleton(self):
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.bind(self.ip,self.port)

        i = 0

        while True:
            msgClient,addr=sock.recvfrom(self.buf_size)

            i = i+1

            thread = SkeletonThread(sock,msgClient,addr,"SKELETON THREAD-"+str(i),self)
            thread.start()
        sock.close()
        
