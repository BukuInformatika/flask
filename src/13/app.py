from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():

 orang = {'nama': 'MIA', 'umur':'20thn'}

 return '''
<html>

    <head>
        <title>Beranda Flask</title>
    </head>

    <body>
        <h1>Hello, ''' + orang['nama'] + ''' Umur Anda, ''' + orang['umur'] + '''!</h1>
    </body>

</html>'''
    
if __name__ =="__main__":
    app.run(debug=True)