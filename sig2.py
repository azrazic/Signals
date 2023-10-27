
import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(-6,6,1000)
d=14/1000

x1=np.heaviside (t-3,1) -np.heaviside(t-4,1)
delta=np.heaviside(t-1,1)- np.heaviside(t-1-d,1)
x=x1+delta
plt.plot(t,x,'y')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid()
