@app.route('/info', methods=['GET'])
def info():
    return str(get_info(get_all_data(dataframe)))