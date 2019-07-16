@app.route('/lang/<string:name>', methods=['DELETE'])
def hapus(name):
langs = [languages for language in languages if language['name'] == name]
languages.remove(langs[0])
return jsonify({'languages': languages})