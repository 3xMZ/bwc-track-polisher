# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 17:34:06 2017

@author: Michael Zhang
"""

from labjack import ljm
import json
import datetime

#Smart Actuator Libraries
import TE_4030_RAW as acc_raw
import TE_HIGH_RAW as acc_high_raw
import Sensor_Profiles as SP


def get_data_and_log(handle):    
    time_current = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    today_date = datetime.datetime.now().date()

    acc_low_x_value,acc_low_y_value,acc_low_z_value = acc_raw.TE_4030_LOW_ACC_RAW(handle,AIN=[0,2,4])
    acc_high_z_val = acc_high_raw.TE_HIGH_ACC_RAW(handle,AIN_names=["AIN6"])
    
    onboard_5V = ljm.eReadName(handle, "AIN8")
    motor_temp_1 = SP.AD22100K(ljm.eReadName(handle, "AIN1"),onboard_5V)
    motor_temp_2 = SP.AD22100K(ljm.eReadName(handle, "AIN3"),onboard_5V)
    system_hum = SP.HIH_4030(ljm.eReadName(handle, "AIN5"))
    #motor_current_1 = ljm.eReadName(handle, "AIN7")
    #motor_current_2 = ljm.eReadName(handle, "AIN9")
    DAQ_temp = SP.LJT7_onboard(ljm.eReadName(handle, "AIN14"))
    
    extra_temp = SP.AD22100K(ljm.eReadName(handle, "AIN10"),onboard_5V) 
    
       
    sensor_data = {
            str(time_current): 
                {
                    'Accelerometer X Raw Fs=400Hz': acc_low_x_value,
                    'Accelerometer Y Raw Fs=400Hz': acc_low_y_value,
                    'Accelerometer Z Raw Fs=400Hz': acc_low_z_value,
                    'High Frequency Accelerometer Z Raw Fs=20,000Hz': acc_high_z_val,
                    'Motor Temperature #1': motor_temp_1,
                    'Motor Temperature #2': motor_temp_2,
                    'System Humidity': system_hum,
                    'Motor Current #1': "NaN",
                    'Motor Current #2': "NaN",
                    'DAQ Temperature': DAQ_temp,
                    'Ambient Temperature' : extra_temp
                }
            }
    try:
        file_name='C:\Log Data\Baseline_'+str(today_date)+'.json'      
        with open(file_name, 'r+', encoding = 'utf-8') as outfile:
            outfile.seek(0,2)
            position = outfile.tell() -1
            outfile.seek(position)
            outfile.write(json.dumps(sensor_data).replace('{',',',1))
    except FileNotFoundError:
        file_name='C:\Log Data\Baseline_'+str(today_date)+'.json'
        with open(file_name, 'w', encoding = 'utf-8') as outfile:
            json.dump(sensor_data, outfile)
        
    return motor_temp_1,motor_temp_2,DAQ_temp,system_hum,time_current,extra_temp    

