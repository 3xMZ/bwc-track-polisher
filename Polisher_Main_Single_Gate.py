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
import Triggered_Collection as TrigC

import Temp_Plot as TPlot
import Environment_Humidity_Plot as HPlot


gate_state =[]
ref_length = 48 # 48 inches are ref length

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
        #tick=time.time()
        #print(time.time())
        motor_temp1,motor_temp2,base_station_temp,env_hum,time_current,ambient_temp=TrigC.get_data_and_log(handle)
        #print(time.time()-tick)
        try:
            TPlot.plot_1(motor_temp1,motor_temp2,base_station_temp,time_current,ambient_temp)
            HPlot.humidity_pie_plot(env_hum)
        except:
            print("Plotly error occured at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ".  Skipping current round of data upload.")
        
        #print("sample taken")
        #print(time.time()-tick)
        time.sleep(0)
        gate_state = [read_gate(handle,"DIO1",gate_state)]
        

# Plotly Login
tls.set_credentials_file(username='mzhang_bwc', api_key='ddyIRzwKNIZUWz5MggDg')
py.sign_in(username='mzhang_bwc', api_key='ddyIRzwKNIZUWz5MggDg')
    
if __name__=='__main__':
#def main():
    print("Data Collection Running...\n")
    
    try:
        file = open("tracklog.txt","a")
        file.write("Track log started at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"\n")
        file.close()
        
        num_track_line = 1
        print("Waiting on track #" + str(num_track_line)+" at "+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"\n")
        gate_state_prev=1
        #error_count = 0
        while True:
            
            gate_state = [read_gate(handle,"DIO1",gate_state_prev)]
            #print("Current Gate State is :" +str(gate_state))
            #print("Previous Gate State is :" +str(gate_state_prev))
            
            if gate_state == ["HIGH"]:
                gate_state_prev=1
                
            elif gate_state == ["FALL"]:
                time_start = time.time()
                #print("Process Start")
                gate_state_prev=0
                
            
            elif gate_state == ["LOW"]:
                gate_state_prev=0
                collect_data(gate_state,handle)
        
                
            elif gate_state == ["RISE"]:
                gate_state_prev=1
                
                time_run = float("{0:.2f}".format(time.time() - time_start))
                print("Track took " + str(time_run)+" seconds to polish.")
                num_track_line +=1
                print("Waiting on track #" + str(num_track_line)+" at "+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"\n")
                file = open("tracklog.txt","a")
                file.write(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+" Track " + str(num_track_line) + " took " + str(time_run)+" seconds to polish. \n")
                file.close()
            
                
    except KeyboardInterrupt:
        ljm.close(handle)

 
    
    