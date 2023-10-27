

import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(-2,2,1000)


# =============================================================================
# Slika 1
# =============================================================================

y1=(2*t +2) * (np.heaviside(t+1,1) - np.heaviside(t+0.5,1))
y2= np.heaviside(t+0.5,1) - np.heaviside(t-0.5,1) 
y3= (-2*t +2)* (  np.heaviside(t-0.5,1) -np.heaviside(t-1,1))
y=y1+y2+y3

plt.plot(t,y, 'r')
plt.xlabel("t")
plt.ylabel("$x_{4}(t)$")
plt.title("Signal 1")
plt.grid()
