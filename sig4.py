
import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(-7,7,1000)
d=14/1000

delta1=np.heaviside(t+5,1)-np.heaviside(t+5-d,1)
delta2=np.heaviside(t-5,1)-np.heaviside(t-5-d,1)
x1=np.heaviside (t+4,1) -np.heaviside(t+1,1)
x2=np.heaviside(t-1,1)- np.heaviside(t-4,1)
x=delta1+x1+x2-delta2
plt.plot(t,x,'b')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Signal 6")
plt.grid()
