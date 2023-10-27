# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 20:38:31 2020

@author: DT User2
"""

import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(-2,2,1000)
y1=(2*t+2)*(np.heaviside(t+1,1)-np.heaviside(t+0.5,1))
y2=(-t-0.5)*(np.heaviside(t+0.5,1)-np.heaviside(t,1))
y3=(t-0.5)*(np.heaviside(t,1)-np.heaviside(t-0.5,1))
y4=(-2*t+2)*(np.heaviside(t-0.5,1)-np.heaviside(t-1,1))
y=y1+y2+y3+y4
plt.plot(t,y,'y')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("signal")
plt.grid()