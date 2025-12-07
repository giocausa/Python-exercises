from concurrent import futures
import grpc
import helloworld_pb2
import helloworld_pb2_grpc

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self,request,context):
        print("[SayHello method invoked] returning response...self: ",hex(id(self)))
        return helloworld_pb2.HelloReply(message="e nu spettacl,%s!"%request.name)

    def SayHelloAgain(self,request,context):
        print("SayHelloAgain method invoked again, returning response...self: ",hex(id(self)))
        return helloworld_pb2.HelloReply(message="CISTIAAAAA,%s!"%request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(),server)

    port = server.add_insecure_port("0.0.0.0:0")

    server.start()

    print("Server start, listening on : "+str(port))

    server.wait_for_termination()

if __name__ =='__main__':
    serve()
    

