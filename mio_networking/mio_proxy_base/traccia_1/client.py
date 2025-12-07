import sys
import threading as mt
import random
from dispatcher_proxy import DispatcherProxy

N_CLIENTS =5

N_reqs_per_client =3

def genera_req_client(host,port):
        for i in range(N_reqs_per_client):
            value_to_deposit = random.randint(0,3)

            thread_name = mt.current_thread().name

            proxy =DispatcherProxy(host,int(port),thread_name,i)
            proxy.sendCmd(value_to_deposit)

if __name__ == '__main__':
    try:
        HOST = sys.argv[1]
        PORT = sys.argv[2]
    except IndexError:
        print("errore nell inserimento di host e port")
        sys.exit(-1)
    
    clients = []

    for i in range(N_CLIENTS):
        t = mt.Thread(target=genera_req_client,args = (HOST,PORT))
        t.start()
        clients.append(t)

    for i in range(N_CLIENTS):
        clients[i].join()

    