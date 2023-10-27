# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 01:22:16 2020

@author: DT User2
"""

import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(-2,2,1000)

y1=(t-1)*(np.heaviside(t+1,1)-np.heaviside(t,1))
y2=(t+1)*(np.heaviside(t,1)-np.heaviside(t-1,1))
x=y1+y2
plt.plot(t,x,'g')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid()
