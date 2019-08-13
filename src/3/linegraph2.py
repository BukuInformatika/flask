from Tkinter import *
import tkFileDialog as filedialog

def line_Graph(self):
        plt.figure(num='Line Graph | File-to-Graph Converter')
        plt.plot(x, marker="o")
        plt.xlabel("Banyak")
        plt.ylabel("Panjang Gelombang")
        plt.show()