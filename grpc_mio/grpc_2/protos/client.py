from __future__ import print_function

import logging ,sys,grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    print("willi willi willi...")

    with grpc.insecure_channel("localhost: "+sys.argv[1])  as channel:

        stub =helloworld_pb2_grpc.GreeterStub(channel)

        response = stub.SayHello(helloworld_pb2.HelloRequest(name = "Chef Franco"))
        print("[CLIENT] Say Hello invoked Greeter Client received: "+ response.message)


        response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name = "CISTIA"))
        print("[CLIENT] SayHelloAgain invoket method Greeter client received: "+response.message)


if __name__ == '__main__':
    run()