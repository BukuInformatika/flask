from flask import Flask, request, jsonify
import pandas as pd

from load_data import load_data
from get_all_data import get_all_data
from get_column import get_column
from get_top_five import get_top_five
from sorting import sorting
from convert_json import convert_json
from insert_data import insert_data
from get_info import get_info
from get_row import get_row
from get_row_field import get_row_field
from get_row_json import get_row_json
from get_all_data_json import get_all_data_json
from jumlah_data import jumlah_data

app = Flask(__name__)

# deklarasi nama file csv
filename = 'Book1.csv'
dataframe = load_data(filename)
dataframe.index += 1

# mengupdate data ketika ada perubahan
def reload_data(fname, dframe):
    global dataframe
    dframe.to_csv(fname, index=False, sep=':')
    dataframe = load_data(fname)

# endpoint localhost:5000/dataset
# endpoint merupakan istilah untuk penyebutan URL API
@app.route('/dataset', methods=['GET'])
def dataset():

# endpoint localhost:5000/jumlah
@app.route('/dataset/jumlah', methods=['GET'])
def jumlah():
    args = request.args
    res = None
    if not len(args) is 0:
        if 'from' in args:
            res = jumlah_data(dataframe, args['from'])
    else:

# endpoint localhost:5000/jumlah
# endpoint localhost:5000/dataset/id id berupa angka
@app.route('/dataset/<int:id>', methods=['GET'])
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
    
@app.route('/info', methods=['GET'])
def info():
    return str(get_info(get_all_data(dataframe)))

if __name__ == "__main__":
    app.run(debug=True)