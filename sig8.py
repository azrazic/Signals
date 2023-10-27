
import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(-2,2,1000)
d=4/1000

x=np.heaviside(t,1)- np.heaviside(t-1,1)
x=np.multiply(x,t)
plt.plot(t,x,'r')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid()
