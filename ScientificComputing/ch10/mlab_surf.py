# -*- coding: utf-8 -*-
import numpy as np
from mayavi import mlab

x, y = np.ogrid[-2:2:200j, -2:2:200j]
z = x * np.exp(- x**2 - y**2)

face = mlab.surf(x, y, z, warp_scale=2)
mlab.axes(xlabel='x', ylabel='y', zlabel='z')
mlab.outline(face)
mlab.show()
