from concurrent import futures
import grpc
import helloworld_pb2
import helloworld_pb2_grpc

class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello_v1(self,request,context):
        for i in range(0,5):
            print("[SERVER] SayHello method invoked, returning response...")
            yield helloworld_pb2.HelloReply(message = "France sei er mejo, "+request.name+ "! -"+str(i))

    def SayHello_v2(self,request_iterator, context):
        names = []
        for request in request_iterator:
            print("[SERVER] Sayhello method invoked, with name: "+request.name)
            names.append(request_iterator)
        return helloworld_pb2.HelloReply(message="Hello, " + ' '.join(names) + "!")
    def SayHello_v3(self,request_iterator,context):

        for request in request_iterator:
            print("[SERVER] SayHello method invoked,returning response...")
            yield helloworld_pb2.HelloReply(message="Daje Danie" +request.name+ " !")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(),server)

    port = server.add_insecure_port("0.0.0.0:0")

    server.start()

    print("server started, listening on : "+str(port))
    server.wait_for_termination()

if __name__ == '__main__':
    serve()