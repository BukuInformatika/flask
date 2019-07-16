def kedua(ukurangmbr, f , g, h,namafile) :
ax = plt.subplot(ukurangmbr)
# Data for plotting
t = np.arange(f, g, h)
s = 1 + np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(xlabel="time (s)", ylabel="voltage (mV)",
title="About as simple as it gets, folks")
ax.grid()
plt.savefig(namafile)