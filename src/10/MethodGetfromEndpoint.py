# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:27:49 2019

@author: Rahmatul Ridha
"""

@app.route('/dataset', methods=['GET', 'POST',
'DELETE'])
def dataset():
 args = request.args
 response = dataframe
 if request.method == 'GET':
 if not len(args) is 0:
 if 'field' in args:
 response = get_column(response,
args['field'])
 if 'topfive' in args:
 response = get_top_five(response,
args['topfive'])
 if 'sort' in args:
 response = sorting(response,
args['sort'])
 if 'format' in args:
 if args['format'] == 'json':
 response = jsonify(get_all_data_json(response))
 else:
 response = str(response)
 else:
 response = str(response)
 return response
