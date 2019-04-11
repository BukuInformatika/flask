def get_top_five(dataframe, order_by):
    return dataframe.head()

@app.route('/dataset', methods=['GET', 'POST', 'DELETE'])
def dataset():
  args = request.args
  response = dataframe
  if request.method == 'GET':
   if 'topfive' in args:
response = get_top_five(response,      args['topfive'])

elif request.method == 'DELETE':
        if not len(args) is 0:
            if 'field' in args:
                response = delete_column(response, args['field'])
