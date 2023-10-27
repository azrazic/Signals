import numpy as np
import matplotlib.pyplot as plt

data = [1, 0, 0, 1, 1, 0, 1, 0]
xs = np.repeat(range(len(data)), 2)
ys = np.repeat(data, 2)
xs = xs[1:]
ys = ys[:-1]
plt.plot(xs, ys)
plt.ylim(-0.5, 1.5)
plt.show()