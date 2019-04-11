# In[1]:
def get_top_five(dataframe, order_by):
    return dataframe.head()
# In[2]:
@app.route('/dataset', methods=['GET', 'POST', 'DELETE'])
def dataset():
  args = request.args
  response = dataframe
  if request.method == 'GET':
   if 'topfive' in args:
response = get_top_five(response,      args['topfive'])