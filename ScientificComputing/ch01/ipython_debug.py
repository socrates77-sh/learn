import numpy as np
import pylab as pl


def test_debug():
    x = np.linspace(1, 50, 10000)
    img = np.sin(x*np.cos(x))
    img.shape = 100, -1
    pl.imshow(img)
    pl.show()


test_debug()
