import grpc,sys
import helloworld_pb2
import helloworld_pb2_grpc

def generate_requests():
    names = ["FRANCESCO","DANIELE","CIRO","THATOTOR"]
    for name_to_send in names:
        yield helloworld_pb2.HelloRequest(name = name_to_send)

def run():
    print("will try to greet world...")

    with grpc.insecure_channel("localhost:"+sys.argv[1]) as channel:

        stub = helloworld_pb2_grpc.GreeterStub(channel)

        print("CALLING SayHello_V1,,,,,,,,,,,,,,")
        for response in stub.SayHello_v1(helloworld_pb2.HelloRequest(name ="pat't")):
            print("[CLIENT] SayHello_1 method invoked greeter client received; "+response.message)
        

        print("CALLING SayHello_v2................")
        response = stub.SayHello_v2(generate_requests())
        print("[CLIENT] invoked SayHello_v2 methods greeater client received: "+response.message)


        print("CALLINGA SayHello_v3.................")
        for response in stub.SayHello_v3(generate_requests()):
            print("[CLIENT] SayHello_v3 invoked greater client received :"+response.message)

if __name__ =='__main__':
    run()


