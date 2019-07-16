from flask import Flask     
app = Flask(__name__)                                                                          
                                                                                                
@app.route('/')                                                                                 
def hello():                                                                                    
   return "Hello World!" 

@app.route('/anu')                                                                                 
def nya():                                                                                    
   return "<h1>GEDE!<h1>" 
 
@app.route('/anu%nya')                                                                                 
def itu():                                                                                    
   return "<h1>panjang!<h1>" 

if __name__ == '__main__':    
   app.run(debug = True)