	self.judul = Label(self.master, text = "File-to-Graph Converter")
        self.judul.grid(row=0,column=1)
        self.label1 = Label(self.master, text = "Pilih File: ",anchor=E, justify=RIGHT)
        self.chooseFile = Button(self.master, text="Browse",command=self.choose_file)
        self.label1.grid(row=1,column=0,ipadx=25)
        self.chooseFile.grid(row=1,column=1,ipadx=20)
        self.txt=Label(self.master, text="*.txt",anchor=W, justify=LEFT)
        self.txt.grid(row=1,column=2,ipadx=25)