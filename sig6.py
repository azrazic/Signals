
import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(-7,7,1000)
x1=np.heaviside(t+4,1)
x2=np.heaviside(t+2,1)
x=-2*(x1-x2)
plt.plot(t,x,'m')
plt.xlabel("t")
plt.ylabel("x(t")
plt.title("signal 2")
plt.grid()
