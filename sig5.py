# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 23:03:27 2020

@author: DT User2
"""

import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(-2,2,1000)

x1=(2*t+2)*(np.heaviside (t+1,1) -np.heaviside(t+0.5,1))
x2=(-t-0.5)*(np.heaviside(t+0.5,1)- np.heaviside(t,1))
x3=(t-0.5)*(np.heaviside(t,1)-np.heaviside(t-0.5,1))
x4=(-2*t+2)*(np.heaviside(t-0.5,1)-np.heaviside(t-1,1))
x=x1+x2+x3+x4
plt.plot(t,x,'b')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Signal $t_4$ ")
plt.grid()
