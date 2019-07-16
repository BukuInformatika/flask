@app.route('/lang/<string:name>', methods=['PUT'])
def editSatu(name):
langs = [languages for language in languages if language['name'] == name]
langs[0] ['name'] = request.json['name']
return jsonify({'language': langs[0]})