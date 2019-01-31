import time
import math
import numpy as np

x = [i * 0.001 for i in range(1000000)]
start = time.process_time()
for i, t in enumerate(x):
    x[i] = math.sin(t)
print("math.sin: %f" % (time.process_time() - start))

x = [i * 0.001 for i in range(1000000)]
x = np.array(x)
start = time.process_time()
np.sin(x, x)
print("numpy.sin: %f" % (time.process_time() - start))

x = [i * 0.001 for i in range(1000000)]
start = time.process_time()
for i, t in enumerate(x):
    x[i] = np.sin(t)
print("math.sin loop: %f" % (time.process_time() - start))
