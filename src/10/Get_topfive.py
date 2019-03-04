def get_top_five(dataframe, order_by):
 return dataframe.head() if order_by == 'first'
else dataframe.tail()