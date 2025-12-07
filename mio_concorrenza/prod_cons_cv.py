import logging
import threading
import time
from random import randint

CONSUMER = 'Consumer'
PRODUCER = 'Producer'
N_PRODUCERS = 10
N_CONSUMERS = 10
QUEUE_SIZE = 5

logging.basicConfig(level=logging.DEBUG,format = '[%(threadName)-0s]%(message)s')

def messaggio_disponibile(queue):
    return not (len(queue) == 0)

def spazio_disponibile(queue):
    return not (len(queue)==QUEUE_SIZE)

def get_item(queue):
    return queue.pop(0)

def make_item(queue):
    item = randint(1,100)
    queue.append(item)
    return item


class consumerThread(threading.Thread):
    def __init__(self,name,queue,consumer_cv,producer_cv):
        threading.Thread.__init__(self, name=name)
        self.producer_cv=producer_cv
        self.consumer_cv=consumer_cv
        self.queue=queue
    
    def run(self):
        logging.debug('\t\t\t start')

        with self.consumer_cv:
            logging.debug('\t\t\t lock ottenuto')
            while not messaggio_disponibile(self.queue):
                logging.debug('\t\t\t non ci sono elementi nella coda')
                self.consumer_cv.wait()
            
            time.sleep(1.0)
            item = get_item(self.queue)
            logging.debug('\t\t\t item : %r',item)

            logging.debug('\t\t\tnotify')
            self.producer_cv.notify()

            logging.debug('\t\t\t lock rilasciato')

def produci(producer_cv,consumer_cv,queue):
    logging.debug('\t\t\tstart produzione')

    with producer_cv:
        logging.debug('\t\t\t lock ottenuto')

        while not spazio_disponibile(queue):
            logging.debug('\t\t\t non ci sono spazi in coda')
            producer_cv.wait()

        time.sleep(1.0)
        item = make_item(queue)
        logging.debug('\t\t\t item : %r',item)

        logging.debug('\t\t\t notify')
        consumer_cv.notify()
        logging.debug('\t\t\t lock rilasciato')

    
def main():
    queue = []
    Consumer = []
    Producer = []

    cv_lock = threading.Lock()
    producer_cv = threading.Condition(cv_lock)
    consumer_cv = threading.Condition(cv_lock)

    for i in range(N_CONSUMERS):
        name = CONSUMER+str(i)
        ct = consumerThread(name,queue,consumer_cv,producer_cv)
        ct.start()
        Consumer.append(ct)

    for i in range (N_PRODUCERS):
        pt = threading.Thread(
            name = PRODUCER+str(i),
            target = produci,
            args=(producer_cv,consumer_cv,queue),
        )
        pt.start()
        Producer.append(pt)
        
    for i in range(N_CONSUMERS):
        Consumer[i].join()
    for i in range(N_PRODUCERS):
        Producer[i].join()

if __name__ == '__main__':
    main()


