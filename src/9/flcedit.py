def img():
        PEOPLE_FOLDER = os.path.join('data', 'img')
        app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER  
   
@app.route('/')
def show_index():
        img()
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'EEG.jpg')    
        return render_template("index.html", user_image = full_filename )