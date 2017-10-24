# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:53:19 2017

@author: mzhang
"""

from labjack import ljm

def TE_HIGH_ACC_RAW(handle,AIN_names):
    
    numAddresses = len(AIN_names)
    aScanList = ljm.namesToAddresses(numAddresses, AIN_names)[0]
    scanRate = 10000
    scansPerRead = scanRate

    aNames = ["AIN_ALL_NEGATIVE_CH", "AIN_ALL_RANGE", "STREAM_SETTLING_US",
              "STREAM_RESOLUTION_INDEX"]
    aValues = [ljm.constants.GND, 10.0, 0, 0] #single-ended, +/-10V, 0 (default),
                                              #0 (default)
    ljm.eWriteNames(handle, len(aNames), aNames, aValues)
    
    # Configure and start stream
    scanRate = ljm.eStreamStart(handle, scansPerRead, numAddresses, aScanList, scanRate)
    
    ret = ljm.eStreamRead(handle)
    
    acc_high_z_val = ret[0]
    
#    acc_high_z_val=[data[i]for i in range(0,len(data),1)]
#    ACC_LOW_Y_value=[data[i]for i in range(1,len(data),3)]
#    ACC_LOW_Z_value=[data[i]for i in range(2,len(data),3)]
    ljm.eStreamStop(handle)
    return acc_high_z_val

