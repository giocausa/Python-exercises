import random,time,sys,socket
from datetime import datetime

BUFFER_SIZE = 1024

if __name__ == '__main__':
    try:
        HOST = sys.argv[1]
        PORT = sys.argv[2]
    except IndexError:
        print("errore nell'inserimento dell'host/port")
        sys.exit(-1)

    cmd_dict = {0:"leggi",1:"scrivi",2:"configurazione",3:"reset"}

    for i in range(15):

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((HOST,int(PORT)))

        message_to_send = "getCmd"

        print(f"[ACTUATOR ]Sending request : {message_to_send}\n")
        time.sleep(1)
        s.send(message_to_send.encode('utf-8'))

        print(f"[ACTUATOR] waiting result for #{i} request\n")
        data = s.recv(BUFFER_SIZE).decode('utf-8')

        print(f"ricevuto il data per la richiesta {i} : {data}...write to file\n")

        with open("cmdLog.txt",mode="a") as cmdlog_file:
            cmdlog_file.write(f'{datetime.now()} {cmd_dict[int(data)]}')
            