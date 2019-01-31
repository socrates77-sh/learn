from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np

font = FontProperties(fname=r'c:\windows\fonts\simsun.ttc', size=14)

# plt.rcParams['font.family'] = 'SimHei'
t = np.linspace(0, 10, 1000)
y = np.sin(t)

plt.plot(t, y)
plt.xlabel(u'时间', FontProperties=font)
plt.ylabel(u'振幅', FontProperties=font)
plt.title(u'正弦波', FontProperties=font)
plt.show()
