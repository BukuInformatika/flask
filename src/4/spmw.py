def ketiga(ukurangmbr,f, g, h,namafile) :
ax = plt.subplot(ukurangmbr)
t1 = np.arange(f, g, h)
for n in [1, 2, 3, 4]:
plt.plot(t1, t1**n, label="n=%d"%(n,))
leg = plt.legend(loc="best", ncol=2, mode="expand", shadow=True, fancybox=True)
leg.get_frame().set_alpha(0.5)
plt.savefig(namafile)