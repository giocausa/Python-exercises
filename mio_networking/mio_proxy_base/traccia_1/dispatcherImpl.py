from dispatcher_service import DispatcherService
import logging
import multiprocess as mp 

logging.basicConfig(level = logging.DEBUG,format="(%(Thread_name)-0s)%(message)s")

class dispatcherImpl(DispatcherService):
    def __init__(self,queue = mp.Queue(5)):
        self.queue = queue
    
    def sendCmd(self,value):
        logging.info(f"[DISPATCHER IMPL]ref to queue: {self.queue}")
        self.queue.put(value)
    
    def getCmd(self):
        value_to_get =self.queue.get()
        logging.info(f"[DISPATCHER IMPL: getCmd] refer to queue: {self.queue}, value: {value_to_get}")
        return value_to_get
        