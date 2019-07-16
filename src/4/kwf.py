def ketiga(ukurangmbr,f, g, h,namafile) :
evenly sampled time at 200ms intervals t = np.arange(f, g, h)
red dashes, blue squares and green triangles plt.plot(t, t, "r--", t, t**2, "bs", t, t**3, "g"") plt.savefig(namafile)