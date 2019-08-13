self.keterangan = Label(self.master, text = "Ubah ke:")
        self.keterangan.grid(row=2, column=1)

        self.lineGraph = Button(self.master, text = "Line Graph",command=self.line_Graph)
        self.lineGraph.grid(row=3,column=0,ipadx=15)