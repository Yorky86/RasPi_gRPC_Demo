# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Built from greeter_client.py in the grpc examples
# 



"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import pumploop_pb2
import pumploop_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    
    print("Will try to greet world ...")
    
    #Some channels to play with
    
    
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = pumploop_pb2_grpc.GreeterStub(channel)
        
        #Request status on all channels
        response = stub.SystemStatus(pumploop_pb2.StsRequest(status = "All"))
        print("System channel status: " + response.message)
        
        #Send update on a control channel
        response = stub.SystemControl(pumploop__pb2.CtrlUpdate(channel
        
        
        #print("Greeter client received: " + response.message)
        #response = stub.SayHello(pumploop_pb2.HelloRequest(name="you"))
        #print("Greeter client received: " + response.message)
        #response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name="you"))
        #print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()
