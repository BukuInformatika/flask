from flask import Flask, render_template, make_response, send_file, url_for
import json, time
import Tkinter
import tkMessageBox
import atexit
from time import clock
import request
import os


app = Flask(__name__)


#
# 
# 
# 
#     
def img():
        PEOPLE_FOLDER = os.path.join('static', 'img')
        app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER        

@app.route('/')
def show_index():
        img()
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'EEG.jpg')       
        return render_template("index.html", user_image = full_filename )


def popup():
        tkMessageBox.showinfo("Information","Created in Python.") 
   
@app.route('/live')                                                      
def live(): 
        popup()
        img()
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'pict.jpg')                
        return render_template('live.html', user = full_filename )                           

dataset = []                             

def myline():
    f = open('tmp','r+')                 
    line = f.readlines()                 
    for x in line:   

                    
        dataset.insert(0,x)             
        return
 
def fromDataset():
        for x in dataset:
                return int(x)     
       
@app.route('/live-data')
def live_data():                                        
    myline()                                            
    data = [time.time() * 500, fromDataset()]             
    print time.ctime(time.time())
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/live-tmp', methods=['GET'])    
def livetmp():
    f = open('tmp','r')                                  
    line = f.readlines()                                 
    for x in line:                                       
        response = make_response(json.dumps(x))                 
        response.content_type = 'application/json'      
        return response  
                              

@app.route('/data', defaults={'req_path':''}, methods=['GET'])
@app.route('/<path:req_path>')

def simpanjson(req_path):
    BASE_DIR = '/Users/PC 10/Zroyek/example2/LIVE/data'
    data_path = os.path.join(BASE_DIR, req_path)                 
    if os.path.isfile(data_path):                                
        return send_file(data_path)
    files = os.listdir(data_path)
    return render_template('files.html', files=files)            
#
#
#
#
#
def secondsToStr(t):#fungsi waktu
    return "%d:%02d:%02d.%03d" % \
        reduce(lambda ll,b : divmod(ll[0],b) + ll[1:], [(t*1000,),1000,60,60])
           
def sapa(nama): 
    print("Hi, " + nama + ". Apa kabar?") 
sapa('teman')                                                  

line = "="*40
def log(s, elapsed=None):                        
    print line
    print secondsToStr(clock()), '-', s          
    if elapsed:
        print "Elapsed time:", elapsed 
    print line
    print
   
def date(): 
        date =time.time
        print time.ctime(time.time())
      
def endlog():
    end = clock()
    elapsed = end-start           
    log("End Program", secondsToStr(elapsed))    
    date() 
    print ('Proyek dua')


def now():
    return secondsToStr(clock())

start = clock()
atexit.register(endlog)
log("Start Program")                             
def print_info( nama, Npm ): 
    print ("Nama: ", nama) 
    print ("Npm: ", Npm) 
print_info( Npm=1164035, nama = "Eko Cahyono Putro" )
print_info( Npm=1164049, nama = "Nur Arkhamia Batubara" )

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)