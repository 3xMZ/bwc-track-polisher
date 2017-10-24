# -*- coding: utf-8 -*-
"""
Created on 8/30/2017

@author: mzhang
"""
#Credential file location C:\Users\<Username>\.plotly\.credentials

import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in(username='mzhang_bwc', api_key='ddyIRzwKNIZUWz5MggDg')

def plot_1(motor_temp1,motor_temp2,base_station_temp,current_time,ambient_temp):
#    motor_temperature1 = go.Scatter(
#        x=[current_time],
#        y=[motor_temp1],
#    )
#    
#    motor_temperature2 = go.Scatter(
#        x=[current_time],
#        y=[motor_temp2]
#    )
#    
#    base_station_temperature = go.Scatter(
#        x=[current_time],
#        y=[base_station_temp]
#    )
#    
#    data = go.Data([motor_temperature1, motor_temperature2, base_station_temperature])
#    
#    # Take 1: if there is no data in the plot, 'extend' will create new traces.
#    plot_url = py.iplot(data, filename='Track Polisher/Temp History', fileopt='extend')
    
    
    trace1 = {
  "x": [current_time],
  "y": [motor_temp1],
  "name" : "Motor #1 Temperature",
  "type": "scatter"
  }
    trace2 = {
  "x": [current_time],
  "y": [motor_temp2],
  "name" : "Motor #2 Temperature",
  "type": "scatter"
  }
    trace3 = {
  "x": [current_time],
  "y": [base_station_temp],
  "name" : "Base Station Temperature",
  "type": "scatter"
  }
    trace4 = {
  "x": [current_time],
  "y": [ambient_temp],
  "name" : "Shop Temperature",
  "type": "scatter"
  }

    data = go.Data([trace1, trace2, trace3, trace4])
    layout = {
  "title": "Temperature Sensor Readings on Track Polisher", 
  "xaxis": {
    "title": "Date and Time", 
    "titlefont": {
      "color": "#7f7f7f", 
      "family": "Roboto, monospace", 
      "size": 18
    }
  }, 
  "yaxis": {
    "title": "Temperature in C", 
    "titlefont": {
      "color": "#7f7f7f", 
      "family": "Roboto, monospace", 
      "size": 18
    }
  }
}
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.iplot(fig, filename='Track Polisher/Temp History', fileopt='extend')
