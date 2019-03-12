# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:20:57 2019

@author: Rahmatul Ridha
"""

def update_data(dataframe, id, newdata):
 dataframe.loc[id, :] = newdata
 return dataframe
