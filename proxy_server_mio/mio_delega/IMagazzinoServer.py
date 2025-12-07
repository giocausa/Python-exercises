from IMagazzinoImpl import IMagazzinoImpl
from IMagazzinoSkeleton import IMagazzinoSkeleton

IP = "localhost"
port = 0
QUEUE_SIZE = 5


magazzino = IMagazzinoImpl(QUEUE_SIZE)
skeleton =  IMagazzinoSkeleton(ip,port,magazzino)
skeleton.runSkeleton()

print("[MAGAZZINO SERVER] started")