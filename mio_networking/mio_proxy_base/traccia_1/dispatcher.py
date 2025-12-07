import sys
from dispatcherImpl import dispatcherImpl
from dispatcher_skeleton import DispatcherSkeleton

if __name__ == '__main__':
    try:
        HOST = sys.argv[1]
        PORT = sys.argv[2]
    
    except IndexError:
        print("errore nell inserimento dei parmetri di connnessione")

    impl =dispatcherImpl()
    skeleton = DispatcherSkeleton(HOST,int(PORT),impl)
    skeleton.run_skeleton()