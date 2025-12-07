import socket
import threading

def th_fun(c):

    data = c.recv(1024)

    data = data[::-1]

    c.send(data)

    c.close()


if __name__ == '__main__':

    host =""
    cur_port = 0

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,cur_port))

    cur_port =s.getsockname()[1]

    print("Socket port : ",cur_port)

    s.listen(5)

    while True:
        c, addr=s.accept()

        print("Connected to: ",addr[0]+":",addr[1])

        t =threading.Thread(target=th_fun,args=(c,))
        t.start()

    s.close()
