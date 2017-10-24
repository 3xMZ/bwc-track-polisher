# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 07:54:49 2017

@author: mzhang
"""

import datetime
import time

start_time = datetime.datetime.now()

while (datetime.datetime.now()-start_time).seconds < 60:
    
    time.sleep(0.5)
    if sensor = "HIGH":
        break
    
    
    # -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 10:10:29 2017

@author: mzhang

Customized for Track Polisher.
Triggered data collection when laser is broken.  Logic for rising and falling edges exist but are unused.
"""
#Updated 8/30/17
#Added humidity and temp plots via plotly


import time
from labjack import ljm

import LJ_Read_Edges as LJR
import Triggered_Collection as TrigC

import Temp_Plot as TPlot
import Environment_Humidity_Plot as HPlot


gate_state =[]

handle=LJR.get_handle()

def read_gate(handle,IO,prev_state): 
       
    if LJR.read_IO(handle,IO) == 1 and prev_state == 1:
        return "HIGH"
        
    elif LJR.read_IO(handle,IO) == 0 and prev_state == 0:
        return "LOW"
    
    elif LJR.read_IO(handle,IO) == 1 and prev_state == 0:
        return "RISE"
    
    elif LJR.read_IO(handle,IO) == 0 and prev_state == 1:
        return "FALL"


def collect_data(gate_state,handle):
    '''
    When laser gate is broken, the DAQ begins burst sampling.
    Temperature data are sent to Plotly.
    '''
    while gate_state==["LOW"]:
        tick=time.time()
        #print(time.time())
        motor_temp1,motor_temp2,base_station_temp,env_hum,time_current=TrigC.get_data_and_log(handle)
        #print(time.time()-tick)  
        
        print("sample taken")
        print(time.time()-tick)
        time.sleep(5)
        gate_state = [read_gate(handle,"DIO1",gate_state)]
        

    
if __name__=='__main__':
#def main():
    try:
        #file = open("testfile.txt","w") 
        num_track_line = 0
        
        gate_state_prev=1
        #error_count = 0
        while True:
            
            gate_state = [read_gate(handle,"DIO1",gate_state_prev)]
            #print("Current Gate State is :" +str(gate_state))
            #print("Previous Gate State is :" +str(gate_state_prev))
            
            if gate_state == ["HIGH"]:
                time_start = 0
                
                #time_run = 0
                gate_state_prev=1
                
            elif gate_state == ["FALL"]:
                #time_start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                #print("Process Start")
                gate_state_prev=0
                
            
            elif gate_state == ["LOW"]:
                gate_state_prev=0
                collect_data(gate_state,handle)
        
                
            elif gate_state == ["RISE"]:
                num_track_line +=1
                #time_run = time.time() - time_start
                #print(str(time_run))
                #file.write(str(time_run))
                #file.write("\n")
                
                gate_state_prev=1
            #time.sleep(100)
    except KeyboardInterrupt:
        ljm.close(handle)

 
    
    