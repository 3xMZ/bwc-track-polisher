# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 17:34:06 2017

@author: Michael Zhang
"""

from labjack import ljm

# Labjack Handle
def get_handle():
    return ljm.openS(deviceType="T7",connectionType="USB",identifier ="ANY")


def read_IO(handle, IO):
    return ljm.eReadName(handle,str(IO))    

def rising_edge_count(handle, IO):
    #Sets selected IO as rising edge counter
    ljm.eWriteName(handle,str(IO)+"_EF_ENABLE",0)
    ljm.eWriteName(handle,str(IO)+"_EF_INDEX",9)
    ljm.eWriteName(handle,str(IO)+"_EF_CONFIG_A",20000)
    ljm.eWriteName(handle,str(IO)+"_EF_CONFIG_B",1)
    ljm.eWriteName(handle,str(IO)+"_EF_ENABLE",1)


def falling_edge_count(handle, IO):
    #Sets selected IO as falling edge counter
    ljm.eWriteName(handle,str(IO)+"_EF_ENABLE",0)
    ljm.eWriteName(handle,str(IO)+"_EF_INDEX",9)
    ljm.eWriteName(handle,str(IO)+"_EF_CONFIG_A",20000)
    ljm.eWriteName(handle,str(IO)+"_EF_CONFIG_B",0)
    ljm.eWriteName(handle,str(IO)+"_EF_ENABLE",1)
    

def read_trigger(handle,IO):
    #if count = 1, returns True    
    if ljm.eReadName(handle,str(IO)+"_EF_READ_A_AND_RESET") ==1:
        return True
    else:
        return False




#if __name__=='__main__':
#    handle= get_handle()
#    falling_edge_count(handle,"DIO1")
#    try:
#        while True:
#            read_trigger()
#    except KeyboardInterrupt:
#        ljm.close(handle)



