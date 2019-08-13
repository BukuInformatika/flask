def kesatu(ukurangmbr, f , h , i,namafile):
ax = plt.subplot(ukurangmbr)
t = np.arange(f, h, i)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)
plt.annotate("local max", xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor="black", shrink=0.05),
)
plt.ylim(-2, 2)
plt.savefig(namafile)