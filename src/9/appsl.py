from flask import Flask

app = Flask(__name__)

@app.route("/sekalilagi")
def  hello():
    return "INI ADALAH HASILNYA!"

if __name__ =="__main__":
    app.run(debug=True)