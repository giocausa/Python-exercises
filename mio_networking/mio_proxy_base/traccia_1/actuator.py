import sys
import threading as mt
from datetime import datetime
from dispatcher_proxy import DispatcherProxy


if __name__ == '__main__':
    try:
        HOST = sys.argv[1]
        PORT = sys.argv[2]
    except IndexError:
        print("inserire port/host corretti ")
        sys.exit(-1)
    
    cmd_dict={0:"Leggi",1:"scrivi",2:"configura",3:"reset"}
    i=0

    while True:
        proxy=DispatcherProxy(HOST,int(PORT),mt.current_thread().name,i)
        data =proxy.getCmd()

        print(f"comando ricevuto per #{i} request: {data}...scrivi su file\n")

        with open("cmdLog.txt",mode="a") as cmdlog_file:
            cmdlog_file.write(f'{datetime.now()} {cmd_dict(int(data))}\n')
        i =i+1