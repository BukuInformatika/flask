@app.route('/dataset/jumlah', methods=['GET'])
def jumlah():
    args = request.args
    res = None
    if not len(args) is 0:
        if 'from' in args:
            res = jumlah_data(dataframe, args['from'])
    else:
        res = jumlah_data(dataframe, 'all')
    return str(res)