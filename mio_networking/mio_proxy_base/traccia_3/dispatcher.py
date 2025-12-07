import sys
from dispatcherImpl import DispatcherImpl
from dispatcherSkeleton import DispatcherSkeleton

if __name__ == '__main__':
    try:
        HOST = sys.argv[1]
        PORT = sys.argv[2]
    except IndexError:
        print("errore nell inserimento di port e host")
        sys.exit(-1)

    impl = DispatcherImpl(HOST,int(PORT))
    impl.run_skeleton()
    