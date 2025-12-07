import threading
import logging
import time
from random import randint

CONSUMER = 'Consumer'
PRODUCER = 'Producer'
N_PRODUCERS = 10
N_CONSUMERS = 10
QUEUE_SIZE = 5

logging.basicConfig(level= logging.DEBUG,format = '[%(threadName)-0s]%(message)s')

def get_item(queue):
    return queue.pop(0)

def make_item(queue):
    item = randint(1,100)
    queue.append(item)
    return item

class consumerThread(threading.Thread):
    def __init__(self,empty,mutex,full,queue,name):
        threading.Thread.__init__(self,name=name)
        self.empty=empty
        self.full=full
        self.mutex=mutex
        self.queue=queue
    def run(self):
        logging.debug('\t\t\t started')
        logging.debug('\t\t\t Check semaforo')

        self.full.acquire()

        with self.mutex:
            time.sleep(1.0)
            item = get_item(self.queue)
            logging.debug('\t\t\t item : %r',item)

        logging.debug('\t\t\t Rilascio il lock')
        self.empty.release()

def produci(mutex,empty,full,queue):
    logging.debug('\t\t\t start produzione')

    logging.debug('check semaforo')

    empty.acquire()

    with mutex:
        time.sleep(1.0)
        item = make_item(queue)
        logging.debug('\t\t\t item : %r',item)

    logging.debug('\t\t\t rilascio il lock')
    full.release()



def main():
    queue = []
    producers = []
    consumers = []

    mutex= threading.Semaphore()
    empty = threading.Semaphore(QUEUE_SIZE)
    full = threading.Semaphore(0)

    for i in range(N_CONSUMERS):
        name = CONSUMER+str(i)

        ct=consumerThread(empty,mutex,full,queue,name)
        ct.start()
        consumers.append(ct)

    for i in range(N_PRODUCERS):
        pt=threading.Thread(
        name=PRODUCER+str(i),
        target=produci,
        args=(mutex,empty,full,queue),
        )
        pt.start()
        producers.append(pt)

    for i in range(N_CONSUMERS):
        consumers[i].join()
    for i in range(N_PRODUCERS):
        producers[i].join()
    
if __name__ == '__main__':
    main()