# -*- coding: utf-8 -*-
"""
Created on 8/30/2017

@author: Michael
"""


import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in(username='mzhang_bwc', api_key='ddyIRzwKNIZUWz5MggDg')

#humidity_value = 80
def humidity_pie_plot(humidity_value):
    humidity_map = [0,60,70,80,90,100]
    color_palette = ["rgb(0,0,155)", "rgb(0,108,255)", "rgb(98,255,146)", "rgb(255,147,0)", "rgb(255,47,0)", "rgb(216,0,0)"]
    hum_color=[]
    
    for i in range(len(humidity_map)):
        if humidity_value>=humidity_map[i]:
            hum_color=color_palette[i]
            
    
    trace1 = {
      "domain": {
        "x": [0, 1], 
        "y": [0, 1]
      }, 
      "hole": 0.75, 
      "hoverinfo": "percent", 
      "labels": ["Relative Humidity"," "], 
      "labelssrc": "mzhang_bwc:38:16cfee", 
      "marker": {
        "colors": [hum_color, "rgb(255,255,255)"], 
        "line": {"width": 4}
      }, 
      "name": "B", 
      "opacity": 1, 
      "pull": 0, 
      "rotation": 0, 
      "sort": False, 
      "textfont": {"size": 15}, 
      "textinfo": "label", 
      "textposition": "outside", 
      "type": "pie", 
      "uid": "d4a860", 
      "values": [humidity_value,100-humidity_value], 
      "valuessrc": "mzhang_bwc:38:213dc5"
    }
    data = go.Data([trace1])
    layout = {
      "annotations": [
        {
          "x": -0.198701298701, 
          "y": -0.359090909091, 
          "ax": 38, 
          "ay": 0, 
          "font": {
            "family": "Droid Sans, sans-serif", 
            "size": 11
          }, 
          "showarrow": True, 
          "text": "", 
          "xanchor": "left", 
          "yanchor": "bottom"
        }
      ], 
      "autosize": False, 
      "hovermode": "closest", 
      "showlegend": False, 
      "title": "Environment Humidity at " + str(humidity_value) + "%"
    }
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.iplot(fig,filename='Track Polisher/Environment Humidity')