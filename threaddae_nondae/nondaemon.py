from threading import*
import time

def check():
    for i in range(5):
        print(f"\t\t\t[thread {i}], ciao bella")
        time.sleep(1)

th = Thread(target=check)
th.start()
time.sleep(3)
print("\t\t\tprogramma terminato")