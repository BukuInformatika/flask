def sorting(dataframe, order_by):
 asc = True if order_by == 'ascending' else
False
 return dataframe.sort_index(ascending=asc)