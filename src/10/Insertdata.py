# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:02:27 2019

@author: Rahmatul Ridha
"""

from get_row_count import get_row_count

def insert_data(dataframe, newdata):
 index = get_row_count(dataframe) + 1
 dataframe.at[index] = newdata