# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:53:19 2017

@author: mzhang
"""

from labjack import ljm

def TE_4030_LOW_ACC_RAW(handle,AIN):

    ACC_L_Address_list = [channel *2 for channel in AIN]
 
    rate, data=ljm.streamBurst(handle, len(ACC_L_Address_list), ACC_L_Address_list, 400, 400)  
  
    ACC_LOW_X_value=[data[i]for i in range(0,len(data),3)]
    ACC_LOW_Y_value=[data[i]for i in range(1,len(data),3)]
    ACC_LOW_Z_value=[data[i]for i in range(2,len(data),3)]
    
    return (ACC_LOW_X_value,ACC_LOW_Y_value,ACC_LOW_Z_value)

