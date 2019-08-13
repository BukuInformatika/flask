import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('hasil.txt', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        

plt.plot(marker='o')

plt.title('Data Gelombang Otak')

plt.xlabel('Banyak Data')
plt.ylabel('Gelombang otak')

plt.show()