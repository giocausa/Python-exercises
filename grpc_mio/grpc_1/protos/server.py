from concurrent import futures

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self,request,context):
        print("[Server] SayHello method invoked, return response...")
        return helloworld_pb2.HelloReply(message = "ER BRASILIANO E QUI CON VOI, %s!" % request.name)

    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(),server)

    port = server.add_insecure_port("0.0.0.0.:0")

    server.start()

    print("server started, listening on port: "+str(port))

    server.wait_for_termination()

if __name__ == "__main__":
    serve()
   