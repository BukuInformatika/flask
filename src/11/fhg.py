@app.route('/lang/<string:name>', methods=['GET'])
def Satu(name):
    langs = [languages for language in languages if language['name'] == name]
    return jsonify({'language': langs[0]})