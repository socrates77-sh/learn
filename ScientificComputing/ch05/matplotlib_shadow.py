import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms

x = np.arange(0, 2, 0.01)
y = np.sin(2*np.pi*x)

N = 7

for i in range(N, 0, -1):
    offset = transforms.ScaledTranslation(
        1, -i, transforms.IdentityTransform())
    shadow_trans = plt.gca().transData+offset
    plt.plot(x, y, linewidth=4, color='black',
             transform=shadow_trans,
             alpha=(N-i)/2/N)

plt.plot(x, y, linewidth=4, color='black')
plt.xlim(0, 2)
plt.ylim(-1.5, 1.5)

plt.show()
