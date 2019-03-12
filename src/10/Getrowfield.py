# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:22:00 2019

@author: Rahmatul Ridha
"""

def get_row_field(dataframe, field):
 return "{}:{}".format(field, dataframe[field])