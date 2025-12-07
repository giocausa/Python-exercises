import random, time, sys,socket

import threading as mt 

BUFFER_SIZE = 1024
N_CLIENTS = 5
N_reqs_per_client = 3


def generate_client_reqs():

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,int(PORT)))

    value_to_deposit = random.randint(0,3)

    request = "sendCmd"
    message_to_send = request + "-"+str(value_to_deposit)
    thread_name = mt.current_thread().name
    print(f"[CLIENT Thread name: {thread_name}] using socket ref {hex(id(s))} ")
    print(f"[CLIENT Thread name: {thread_name}] \t\t\tsending request #{i} message: {message_to_send}")

    time.sleep(random.randint(2,4))
    s.send(message_to_send.encode('utf-8'))

    print(f"[CLIENT Thread name: {thread_name}] waiting for result")
    data = s.recv(BUFFER_SIZE).decode('utf-8')
    print(f"[CLIENT Thread name: {thread_name}] \t\t\t data received: {data:s} for #{i} request\n")
    
    s.close()

if __name__ == '__main__':
    try:
        HOST = sys.argv[1]
        PORT = sys.argv[2]
    except IndexError:
        print("errore nell'inserimento del port/host")
        sys.exit(-1)

    clients = []
    for i in range(N_CLIENTS):
        cl = mt.Thread(target=generate_client_reqs)
        cl.start()
        clients.append(cl)

    for i in range(N_CLIENTS):
        clients[i].join()
        