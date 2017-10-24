# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 17:39:37 2017

@author: Michael
"""
#Sensor Profiles

#Temperature Sensor
def AD22100K(voltage,v_ref):
    #(voltage-1.375)*1000/(22.5)
    return (voltage*(5/v_ref)-1.375) *1000 / 22.5 #in Celsius

def LJT7_onboard(voltage):
    TempK=voltage*-92.6 + 467.6
    return (TempK-273.15)

#Humidity Sensor
def CHS_UGR(voltage):
    return float("{0:.2f}".format(voltage*100))

def CHS_UPR(voltage):
    return float("{0:.2f}".format(voltage*100))

def HIH_4030(voltage):
    return float("{0:.2f}".format((voltage-0.958)/0.03068))


#Accelerometer
def TE_4030_LOW_ACC(voltage):
    return (voltage -2.5)*1000/333

#Current Transducer
def CR5210S(voltage):
    return voltage*5 #Assuming linear behavior


