import sys,random
import threading as mt
from dispatcher_proxy import DispatcherProxy

N_CLIENTS = 5
N_reqs_per_client =3

def generate_client_reqs(host,port):
        for i in  range(N_reqs_per_client):
            value_to_deposit =random.randint(0,3)

            thread_name = mt.current_thread().name

            proxy = DispatcherProxy(host,int(port),thread_name,i)

            proxy.sendCmd(value_to_deposit)


if __name__ =='__main__':
    try:
        HOST = sys.argv[1]
        PORT = sys.argv[2]
    except IndexError:
        print("errore nell inserimento di port e host")
        sys.exit(-1)

    clients = []

    for i in range(N_CLIENTS):
        c = mt.Thread(target=generate_client_reqs,args=(HOST,PORT))
        c.start()
        clients.append(c)

    for i in range(N_CLIENTS):
        clients[i].join()
        
