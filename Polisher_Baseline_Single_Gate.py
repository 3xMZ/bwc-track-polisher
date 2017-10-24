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
import datetime
from labjack import ljm
import plotly.tools as tls
import plotly.plotly as py

import LJ_Read_Edges as LJR
import Baseline_Collection as BaseC

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
    while gate_state==["HIGH"]:
        tick=time.time()

        motor_temp1,motor_temp2,base_station_temp,env_hum,time_current,ambient_temp=BaseC.get_data_and_log(handle)

        try:
            TPlot.plot_1(motor_temp1,motor_temp2,base_station_temp,time_current,ambient_temp)
            HPlot.humidity_pie_plot(env_hum)        
        except:
            print("Error occured at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ".  Skipping current round of data upload.")
            
        print(time.time()-tick)

        gate_state = [read_gate(handle,"DIO1",gate_state)]
        

# Plotly Login
tls.set_credentials_file(username='mzhang_bwc', api_key='ddyIRzwKNIZUWz5MggDg')
py.sign_in(username='mzhang_bwc', api_key='ddyIRzwKNIZUWz5MggDg')
    
if __name__=='__main__':
    try:
        count = 0
        
        gate_state_prev=1
        while count <5:
            
            gate_state = [read_gate(handle,"DIO1",gate_state_prev)]
            
            if gate_state == ["HIGH"]:
                print("High")
                collect_data(gate_state,handle)
                gate_state_prev=1
                
            elif gate_state == ["FALL"]:
                gate_state_prev=0
                
            
            elif gate_state == ["LOW"]:
                gate_state_prev=0
                
        
                
            elif gate_state == ["RISE"]:
                gate_state_prev=1
                
            count+=1
    except KeyboardInterrupt:
        ljm.close(handle)
ljm.close(handle)

 
    
    