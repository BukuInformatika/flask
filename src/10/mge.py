@app.route('/dataset/<int:id>', methods=['GET', 'POST', 'DELETE'])
def detail(id):
    args = request.args
    detailframe = get_row(get_all_data(dataframe), id)
    if request.method == 'GET':
        if not len(args) is 0:
            if 'field' in args:
                detailframe = get_row_field(detailframe, args['field'])
            if 'format' in args:
                if args['format'] == 'json' and 'field' not in args:
                    detailframe = jsonify(get_row_json(detailframe))
else:
                    return jsonify(detailframe)
  else:
                detailframe = str(detailframe)
        else:
            detailframe = str(detailframe)
        return detailframe