from flask import Flask 
app = Flask(__name__)

@app.route('/<contoh2>')
def index(contoh2):
    return contoh2
    
if __name__ =="__main__":
    app.run(debug=True)