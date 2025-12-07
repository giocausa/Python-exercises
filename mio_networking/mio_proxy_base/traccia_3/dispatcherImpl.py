from dispatcherSkeleton import DispatcherSkeleton
import multiprocess as mp 

class DispatcherImpl(DispatcherSkeleton):

    def __init__(self,host,port, queue = mp.Queue(5)):
        super().__init__(host,port)
        self.queue = queue

    def sendCmd(self,value):
        self.queue.put(value)
    def getCmd(self):
        return self.queue.get()