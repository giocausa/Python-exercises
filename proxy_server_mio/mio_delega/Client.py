from threading import Thread,current_thread
from IMagazzinoProxy import IMagazzinoProxy

import sys,random,time


def thread_fun(service,ip,port,num_reqs):
    waiting_time =randint(1,100)
    time.sleep(waiting_time)

    proxy=IMagazzinoProxy(ip,port)

    for i in range(num_reqs):

        choice = randint(1,100)

        if choice == 0:
            articolo = "smartphone"
        else:
            articolo = "laptop"
        
        if service == "deposita":
            id = random.randint(1,100)

            print(f"[{current_thread().name}] Sending request {service}, {articolo}, {id}")

            result = proxy.deposita(articolo,id)

            if not result:
                print(f"[{current_thread().name}] {service},{articolo},{id} failed")
            else:
                print(f"[{current_thread().name}] {service},{articolo},{id} success")

        elif service == "preleva":

            print(f"[{current_thread().name}], Send request {service}, {articolo}")

            result = proxy.preleva(articolo)

            if result==-1:
                print(f"[{current_thread().name}] {service},{articolo} failed")
            else:
                print(f"[{current_thread().name}] {service},{articolo} success, ID= {str(result)}")

            
NUM_THREADS =5
NUM_REQS_THREADS =3
IP = 'localhost'

try:
    service = sys.argv[1]
    port = int(sys.argv[2])
except IndexError:
    print("[CLIENT] Missing name service name and/or server port parameters")
    sys.exit(-1)


threads = []

for i in range(NUM_THREADS):

    th = Thread(target=thread_fun,args=(service,IP,port,NUM_REQS_THREADS),name="CLIENT THREAD"+str(i))
    th.start()
    threads.append(th)

for i in range(NUM_THREADS):
    threads.pop().join()




