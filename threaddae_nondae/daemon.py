from threading import*
import time

def fun():
    for i in range(5):
        print("\t\t\til mio pisello è lunghissimo e pelosissimo")
        time.sleep(1.0)

thread = Thread(target=fun,daemon=True)
thread.start()
time.sleep(4.0)
print("\t\t\tprogramma terminato")
        

