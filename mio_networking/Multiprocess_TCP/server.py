import socket
import multiprocess as mp

def multi_fun(c):
    
    data = c.recv(1024)

    data = data [::-1]

    c.send(data)

    c.close()

if __name__ == '__main__':
    host = ""
    curr_port =0

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,curr_port))
    curr_port= s.getsockname()[1]

    print("socket binded to port ",curr_port)

    s.listen(5)

    while True:
        c, addr =s.accept()

        print("connect to: ",addr[0],"-",addr[1])

        p = mp.Process(target=multi_fun,args = (c,))
        p.start()

    s.close()
