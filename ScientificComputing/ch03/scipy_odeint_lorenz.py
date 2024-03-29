import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def lorenz(w, t, p, r, b):
    x, y, z = w.tolist()
    return p*(y-x), x*(r-z)-y, x*y-b*z


t = np.arange(0, 30, 0.01)
track1 = odeint(lorenz, (0, 1, 0), t, args=(10, 28, 3))
track2 = odeint(lorenz, (0, 1.01, 0), t, args=(10, 28, 3))

fig = plt.figure()
ax = Axes3D(fig)

ax.plot(track1[:, 0], track1[:, 1], track1[:, 2])
ax.plot(track2[:, 0], track2[:, 1], track2[:, 2])

plt.show()
