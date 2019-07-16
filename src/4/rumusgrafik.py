def kelima(d,i,xlabel,ylabel,title,namafile) :
#Fixing random state for reproducibility 
np.random.seed(19680801)
mu, sigma = d,i
x = mu + sigma * np.random.randn(10000)
# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor="g", alpha=0.75)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.text(60, .025, r"$\mu=100,\ \sigma=15$")
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.savefig(namafile)