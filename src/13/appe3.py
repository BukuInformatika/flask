from flask import Flask, render_template

app = Flask(__name__)

app = Flask(__name__)

@app.route('/')

def hello_world():
    
    orang = {'nama': 'MIA', 'umur':'20thn'}
    
    return render_template('index.html', title='Beranda', orang=orang)
    
if __name__ =="__main__":
    app.run(debug=True)