@app.route('/') ## Mendefiniskan URL
@app.route('/index', methods=['GET', 'POST'])
def show_index(): #membuat fungsi show_index
full_filename  = os.path.join(app.config['UPLOAD_FOLDER'],'brainwave.png') ##mengambil dan menampilkan gambar yang telah dipilih untuk ditampilkan
return render_template("matplotlib.html", user_image = full_filename) ## memanggil template html yang digunakan sebagai wadah untuk menampilkan gambar dari sintak sebelumnya pada web browser