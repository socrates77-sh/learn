import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def func(x, y):
    return (x+y)*np.exp(-5*(x**2+y**2))


y, x = np.mgrid[-1:1:15j, -1:1:-15j]

fvals = func(x, y)

newfunc = interpolate.interp2d(x, y, fvals, kind='cubic')

xnew = np.linspace(-1, 1, 100)
ynew = np.linspace(-1, 1, 100)

xnew = newfunc(xnew, ynew)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x, y, fvals, marker='.', c='r')
ax.plot_surface(xnew, xnew, xnew, color='y')

# plt.contour(x, y, fvals)
# pl.legend(loc='lower right')
plt.show()
