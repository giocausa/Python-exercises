from __future__ import print_function

import logging,sys,grpc,helloworld_pb2,helloworld_pb2_grpc

def run():
    print("ECCHIME BRASILIA...")

    with grpc.insecure_channel("localhost: "+sys.argv[1]) as channel:

        stub = helloworld_pb2_grpc.GreeterStub(channel)

        response =stub.SayHello(helloworld_pb2.HelloRequest(name = "Minnocci"))
        print("[CLIENT] SayHello invoked Greeter Client received "+ response.message)

if __name__ == '__main__':
    run()