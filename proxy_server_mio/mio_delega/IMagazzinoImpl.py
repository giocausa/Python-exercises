from IMagazzino import IMagazzino
from threading import Lock,Condition

class IMagazzinoImpl(IMagazzino):
    def __init__(self,queue_size = 5):

        self.laptop_queue=[]
        self.smartphone_queue=[]


        smartphone_lock = Lock()
        laptop_lock = Lock()


        self.cv_laptop_producer = Condition(laptop_lock)
        self.cv_laptop_consumer = Condition(laptop_lock)
        
        self.cv_smartphone_producer = Condition(smartphone_lock)
        self.cv_smartphone_consumer = Condition(smartphone_lock)

        self.laptop_file_name ='laptop.txt'
        self.smartphone_file_name ='smartphone.txt'

        laptop_file = open(self.laptop_file_name,'a')
        laptop_file.truncate(0)
        laptop_file.close()
        smartphone_file = open(self.smartphone_file_name, 'a')
        smartphone_file.truncate(0)
        smartphone_file.close()

    def spazio_disponibile(self,queue):
        return not (len(queue) == self.queue_size)
    def messaggio_disponibile(self,queue):
        return not(len(queue) == 0)

    def deposita(self,articolo,id):
        success==True
        if articolo == "laptop":

            with self.cv_laptop_producer:
                while not spazio_disponibile(self.laptop_queue):
                    self.cv_laptop_producer.wait()
                self.laptop_queue.append(id)
                printf(f'[MAGAZZINO IMPL] Add {id} in {articolo}')

                self.cv_laptop_consumer.notify()
        
        elif articolo == "smartphone":

            with cv_smartphone_producer:
                while not self.spazio_disponibile(self.smartphone_queue):
                    self.cv_smartphone_producer.wait()
                self.smartphone_queue.append(id)
                printf(f'[MAGAZZINO IMPL] Add {id} in {articolo}')

                self.cv_smartphone_consumer.notify()
        else:
            print('[MAGAZZINOIMPL] articolo non riconosciuto')
            success = False
        return success


    def preleva(self,articolo):
        id = -1
        if articolo == "laptop":
            with self.cv_laptop_consumer:
                while not self.messaggio_disponibile(self.laptop_queue):
                    self.cv_laptop_consumer.wait()
            
                self.laptop_queue.pop(0)
                printf(f'[MAGAZZINO IMPL] prelevato {id} da {articolo}')

                with open(self.laptop_file_name,'a') as file:
                    file.write(str(id)+"\n")
            
            self.cv_laptop_producer.notify()

        elif articolo == "smartphone":
            with self.cv_smartphone_consumer:
                while not self.messaggio_disponibile(self.smartphone_queue):
                    self.cv_smartphone_consumer.wait()
                self.smartphone_queue.pop(0)
                printf(f'[MAGAZZINO IMPL] prelevato {id} da {articolo}')

                with open(self.smartphone_file_name,'a')as file:
                    file.write(str(id)+"\n")
                
                self.cv_smartphone_producer.notify()
        else:
             print('[MAGAZZINOIMPL] articolo non riconosciuto')
           
        return id

                
                




