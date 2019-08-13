import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('hasil.txt', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[0]))


plt.scatter(x,y, facecolor='red')

plt.title('Data Gelombang Otak')

plt.xlabel('Banyak Data')
plt.ylabel('Gelombang otak')

plt.show()