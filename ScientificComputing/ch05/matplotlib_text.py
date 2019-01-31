import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 10)
y = x**2

plt.rcParams['font.family'] = 'FangSong'
fig = plt.figure(figsize=(8, 4))
ax = plt.subplot(111)
plt.plot(x, y)

for i, (_x, _y) in enumerate(zip(x, y)):
    plt.text(_x, _y, str(i), color='red', fontsize=i+10)

plt.text(0.5, 0.8, u'子坐标系中的文字', color='blue',
         ha='center', transform=ax.transAxes)

plt.figtext(0.1, 0.92, u'图表坐标系中的文字', color='green')

plt.show()
