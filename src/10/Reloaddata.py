# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:26:49 2019

@author: Rahmatul Ridha
"""

def reload_data(filename, dataframe):
 dataframe.to_csv(filename, index=False, sep=':')