def delete_all_data(dataframe):
    dataframe.drop(['raw_value'], axis=1)