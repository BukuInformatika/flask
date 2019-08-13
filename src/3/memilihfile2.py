def choose_file(self):
        file_name = filedialog.askopenfilename()
        if not file_name:
            return
        for line in open(file_name, 'r'):
            values = [float(s) for s in line.split()]
            x.append(values[0])
            y.append(values[0])
            self.adaFile["text"]="File sudah tersedia!"