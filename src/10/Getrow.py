# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:20:06 2019

@author: Rahmatul Ridha
"""

def get_row(dataframe, id):
 return dataframe.loc[id, ['raw_value', 'data',
'sign']]