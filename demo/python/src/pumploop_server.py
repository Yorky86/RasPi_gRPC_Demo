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
# Built from greeter_server.py in the grpc examples
# 
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
from numpy import random
import time
import logging

import grpc
import pumploop_pb2 as pumploop_messages
import pumploop_pb2_grpc as pumploop_services

#Is this possible, would it work to define them here
node = pumploop_messages.SystemInfo
node.nodeID = 101
node.nodeDescription = "RasPi 5"
node.statusMsg = "Running..."

valves = pumploop_messages.Valves
valves.tankFillIV = False
valves.tankOutIV = False
valves.tankDrainIV = False
valves.dutInIV = False
valves.dutOutIV = False
valves.sumpDrainIV = False

sensors = pumploop_messages.Sensors
sensors.tankLevel    = 30
sensors.tankTemp     = 18
sensors.dutFlow      = 25
sensors.pumpTemp     = 30  
sensors.pumpSpeed    = 50
sensors.dutPressIn   = 5.2
sensors.dutPressOut  = 1.2
sensors.dutTemp      = 38
sensors.sumpLevel    = 5
sensors.ambientTemp  = 22
sensors.ambientPress = 1.01

controls = pumploop_messages.Controls
controls.pumpEnable = False
controls.pumpDemand = 0
controls.sumppumpEnable = False

tankDrainRate = 3
tankFillRate = 2
tankTempDriftRateUp = 0.2
dutTempDriftRateUp = 1.2
pumpTempDriftRateUp = 3
tankTempDriftRateDown = 0.1
dutTempDriftRateDown = 0.6
pumpTempDriftRateDown = 1.2
dutNominalWorkingTemp = 50
dutNominalWorkingPress = 7
dutPressureDelta = 3.8
nominalPumpTemp = 40
baseAmbientTemp = 18
baseAmbientPressure = 1
systemCapacity = 5
systemPressureRampRate = 0.5
tankHighLevelCutoff = 90
dutFlowRampRateUp = 5
dutFlowRampRateDown = 15
processUpdatePeriod = 0.25



class PumpController(pumploop_services.PumpControllerServicer):


    #definitions from proto for ref
    #rpc SetSystemInfo (SetSysInfoRequest) returns (SetSysInfResult) {}
    #rpc GetSystemInfo (GetSysInfRequest) returns (SystemInfo) {}
    #rpc SetValveStatus (SetValveRequest) returns (SetValveResult) {}    
    #rpc GetValveStatus (GetValveRequest) returns (GetValveResult) {}
    #rpc GetSensorReading (GetSensorRequest) returns (GetSensorResult) {}
    #rpc GetSensorStream (GetSensorRequest) returns (stream GetSensorResult) {}
    #rpc SetSystemControl (CtrlUpdateRequest) returns (CtrlUpdateResult) {}
    #rpc GetSystemControl (GetControlValue) returns (GetControlResult) {}
            
    def SetSystemInfo(self, request, context):
        #node = pumploop_messages.SystemInfo(nodeID = request.nodeID, nodeDescription = request.nodeDescription)
        node.nodeID = request.nodeID
        node.nodeDescription = request.nodeDescription
        node.statusMsg = "Node info initialised" 
        return pumploop_messages.SystemInfo(nodeID = node.nodeID,
                                            nodeDescription = node.nodeDescription,
                                            statusMsg = node.statusMsg)
        
    def GetSystemInfo(self, request, context):
        return pumploop_messages.SystemInfo(nodeID = node.nodeID,
                                            nodeDescription = node.nodeDescription,
                                            statusMsg = node.statusMsg)
    
    def SetValveStatus(self, request, context):
        valves.tankFillIV = request.tankFillIV
        valves.tankOutIV = request.tankOutIV
        valves.tankDrainIV = request.tankDrainIV
        valves.dutInIV = request.dutInIV
        valves.dutOutIV = request.dutOutIV
        valves.sumpDrainIV = request.sumpDrainIV
        return pumploop_messages.Valves(tankFillIV = valves.tankFillIV,
                                        tankOutIV = valves.tankOutIV,
                                        tankDrainIV = valves.tankDrainIV,
                                        dutInIV = valves.dutInIV,
                                        dutOutIV = valves.dutOutIV,
                                        sumpDrainIV = valves.sumpDrainIV)
                
    def GetValveStatus(self, request, context):
        return pumploop_messages.Valves(tankFillIV = valves.tankFillIV,
                                        tankOutIV = valves.tankOutIV,
                                        tankDrainIV = valves.tankDrainIV,
                                        dutInIV = valves.dutInIV,
                                        dutOutIV = valves.dutOutIV,
                                        sumpDrainIV = valves.sumpDrainIV)
    
    def GetSensorReading(self, request, context):
        return pumploop_messages.Sensors(tankLevel = sensors.tankLevel,
                                         tankTemp = sensors.tankTemp,
                                         dutFlow = sensors.dutFlow,
                                         pumpTemp = sensors.pumpTemp,
                                         pumpSpeed = sensors.pumpSpeed,
                                         dutPressIn = sensors.dutPressIn,
                                         dutPressOut = sensors.dutPressOut,
                                         dutTemp = sensors.dutTemp,
                                         sumpLevel = sensors.sumpLevel,
                                         ambientTemp = sensors.ambientTemp,
                                         ambientPress = sensors.ambientPress)
            
    def GetSensorStream(self, request, context):
        yield pumploop_messages.Sensors(tankLevel = sensors.tankLevel,
                                         tankTemp = sensors.tankTemp,
                                         dutFlow = sensors.dutFlow,
                                         pumpTemp = sensors.pumpTemp,
                                         pumpSpeed = sensors.pumpSpeed,
                                         dutPressIn = sensors.dutPressIn,
                                         dutPressOut = sensors.dutPressOut,
                                         dutTemp = sensors.dutTemp,
                                         sumpLevel = sensors.sumpLevel,
                                         ambientTemp = sensors.ambientTemp,
                                         ambientPress = sensors.ambientPress)
    
    def SetSystemControl(self, request, context):
        controls.pumpEnable = request.pumpEnable
        controls.pumpDemand = request.pumpDemand
        controls.sumppumpEnable = request.sumppumpEnable
        return pumploop_messages.Controls(pumpEnable = controls.pumpEnable,
                                          pumpDemand = controls.pumpDemand,
                                          sumppumpEnable = controls.sumppumpEnable)
                
    def GetSystemControl(self, request, context):
        return pumploop_messages.Controls(pumpEnable = controls.pumpEnable,
                                          pumpDemand = controls.pumpDemand,
                                          sumppumpEnable = controls.sumppumpEnable)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pumploop_services.add_PumpControllerServicer_to_server(PumpController(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    print("Calling process model")
    systemControlLoop()
    server.wait_for_termination()

def systemControlLoop():
    print("Process model started...")
    outputUpdateCounter = 0
    processUpdate = False
    systemIdle = False
    previousTick = time.time()
    thisTick = time.time()
    while 1:
        #print(thisTick-previousTick)
        if thisTick - previousTick >= processUpdatePeriod:
            processUpdate = True
            previousTick = time.time()
            thisTick = time.time()
            #print("Tick")
            
        #Process
        systemIdle = True
        if processUpdate:
            #Make ambient sensors "wiggle"
            sensors.ambientTemp = random.uniform(baseAmbientTemp-0.5,baseAmbientTemp+0.5)
            sensors.ambientPressue = random.uniform(baseAmbientPressure-0.1, baseAmbientPressure+0.1)
            
            #Tank drain handler
            if valves.tankDrainIV and (valves.tankFillIV != 1) :
                node.statusMsg = "Tank draining."
                systemIdle = False
                if sensors.tankLevel > tankDrainRate :
                    sensors.tankLevel = sensors.tankLevel - tankDrainRate
                else:
                    sensors.tankLevel = 0
            elif valves.tankFillIV:
                valves.tankDrainIV = 0
            
            #Tank fill handler
            if valves.tankFillIV and (valves.tankDrainIV != 1) :  
                node.statusMsg = "Tank filling."
                systemIdle = False
                if sensors.tankLevel < tankHighLevelCutoff :
                    sensors.tankLevel = sensors.tankLevel + tankFillRate
                else:
                    valves.tankFillIV = False
            elif valves.tankDrainIV:
                valves.tankFillIV = 0
            
            #Sump drain handler
            if valves.sumpDrainIV and processUpdate:
                node.statusMsg = "Sump drain open"
                systemIdle = False
                if controls.sumppumpEnable :
                    node.statusMsg = "Sump drain open and sump is draining..."
                    systemIdle = False
                    sensors.sumpLevel -= 0.1
            else:
                controls.sumppumpEnable = 0
            
            if controls.pumpEnable: #pump is on
                if valves.tankOutIV and valves.dutInIV and valves.dutOutIV and (valves.tankFillIV != 1) and (valves.tankDrainIV != 1):
                    node.statusMsg = "Pump running, system flowing"
                    systemIdle = False
                    #Pressure ramp up
                    if sensors.dutPressIn < (dutNominalWorkingPress - 0.4):
                        sensors.dutPressIn += systemPressureRampRate
                    else:
                        sensors.dutPressIn = random.uniform(dutNominalWorkingPress-0.2, dutNominalWorkingPress+0.2)
                    sensors.dutPressOut = sensors.dutPressIn - dutPressureDelta
                    
                    #DUT Temp ramp up
                    if sensors.dutTemp  < (dutNominalWorkingTemp - 1):
                        sensors.dutTemp += dutTempDriftRateUp
                    else:
                        sensors.dutTemp = random.uniform(dutNominalWorkingTemp-0.5, dutNominalWorkingTemp+0.5)
                        
                    #Tank Temp ramp up
                    if sensors.tankTemp  < (dutNominalWorkingTemp - 1):
                        sensors.tankTemp += tankTempDriftRateUp
                    else:
                        sensors.tankTemp = random.uniform(dutNominalWorkingTemp-0.5, dutNominalWorkingTemp+0.5)

                    #Pump Temp ramp up
                    if sensors.pumpTemp  < (nominalPumpTemp - 1):
                        sensors.pumpTemp += pumpTempDriftRateUp
                    else:
                        sensors.pumpTemp = random.uniform(nominalPumpTemp-0.5, nominalPumpTemp+0.5)

                    #Flow ramp up
                    if sensors.dutFlow  < (controls.pumpDemand - 1):
                        sensors.dutFlow += pumpTempDriftRateUp
                    else:
                        sensors.dutFlow = random.uniform(controls.pumpDemand-1, controls.pumpDemand+1)
                        
                    sensors.sumpLevel += 0.1 
                else:
                    node.statusMsg = "Pump running but at least one valve is closed"   
                    systemIdle = False
                    sensors.dutPressIn = 0.6
                    sensors.dutPressOut = 1
                    sensors.dutFlow = 0
                    
                        
            else:   #pump off, ramp down 
                #Pressure ramp down
                if sensors.dutPressIn > systemPressureRampRate:
                    sensors.dutPressIn -= systemPressureRampRate
                else:
                    sensors.dutPressIn = 0
                #on the way down, when the inlet pressure goes below the differential, outlet is 1 bar
                if sensors.dutPressOut > 1:
                    sensors.dutPressOut = sensors.dutPressIn - dutPressureDelta
                else:
                    sensors.dutPressOut = 1
                
                #DUT Temp ramp down
                if sensors.dutTemp  > (baseAmbientTemp + 1.5):
                    sensors.dutTemp -= dutTempDriftRateDown
                else:
                    sensors.dutTemp = random.uniform(baseAmbientTemp-0.5, baseAmbientTemp+0.5)
                
                #Tank Temp ramp down
                if sensors.tankTemp  > (baseAmbientTemp + 1.5):
                    sensors.tankTemp -= tankTempDriftRateDown
                else:
                    sensors.tankTemp = random.uniform(baseAmbientTemp-0.5, baseAmbientTemp+0.5)
                    
                #Pump Temp ramp down
                if sensors.pumpTemp  > (controls.pumpDemand + 10):
                    sensors.pumpTemp -= dutFlowRampRateDown
                else:
                    sensors.pumpTemp = 0
                    
                #Flow ramp down
                if sensors.dutFlow  > (controls.pumpDemand + 10):
                    sensors.dutFlow -= dutFlowRampRateDown
                else:
                    sensors.dutFlow = 0
            
            if controls.pumpEnable == 1:
                sensors.pumpSpeed = controls.pumpDemand / 10
            else:
                sensors.pumpSpeed = 0
            
            if systemIdle: node.statusMsg = "System Idle"
            """if outputUpdateCounter >= 4 :
                outputUpdateCounter = 0
                print(node.statusMsg)
            else:
                outputUpdateCounter += 1"""
            
        processUpdate = False
        thisTick = time.time()
        
                    
        #Interlocking
                    

"""tankDrainRate = 1
tankTempDriftRate = 0.2
dutTempDriftRate = 1.2
dutNominalWorkingTemp = 50
dutNominalWorkingPress = 7
dutPressureDelta = 3.8
nominalPumpTemp = 40
baseAmbientTemp = 18
baseAmbientPressure = 1
systemCapacity = 5
"""
    

if __name__ == "__main__":
    logging.basicConfig()
    serve()
    
