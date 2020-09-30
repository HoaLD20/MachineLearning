import matplotlib.pyplot as plt
import scipy as sp
import numpy


def error(f, x, y):
    return sp.sum((f(x) - y) ** 2)


data = numpy.genfromtxt("web_traffic.tsv", delimiter="\t")
x = data[:, 0]
y = data[:, 1]
x = x[~numpy.isnan(y)]
y = y[~numpy.isnan(y)]
plt.scatter(x, y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w * 7 * 24 for w in range(10)],
           ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()

fp1, residuals, rank, sv, rcond = numpy.polyfit(x, y, 1, full=True)
f1 = numpy.poly1d(fp1)
fx = numpy.linspace(0, x[-1], 1000)  # generate X-values for plotting
plt.plot(fx, f1(fx), linewidth=4)
plt.legend(["d=%i" % f1.order], loc="upper left")
inflection = 3.5 * 7 * 24  # calculate the inflection point in hours
xa = x[:inflection]  # data before the inflection point
ya = y[:inflection]
xb = x[inflection:]  # data after
yb = y[inflection:]
fa = sp.poly1d(sp.polyfit(xa, ya, 1))
fb = sp.poly1d(sp.polyfit(xb, yb, 1))
fa_error = error(fa, xa, ya)
fb_error = error(fb, xb, yb)
print("Error inflection=%f" % (fa + fb_error))
