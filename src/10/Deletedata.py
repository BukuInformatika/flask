# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:20:45 2019

@author: Rahmatul Ridha
"""

def delete_data(dataframe, id):
6
 id = int(id) if type(id) != int else id
 dataframe.drop([id], axis=0, inplace=True)
 return dataframe
