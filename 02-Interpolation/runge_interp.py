#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 16:00:47 2022

@author: Analabha Roy
"""

import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

def runge(x):
    return 1/(1 + 25 * x**2)

x = np.arange(-1., 1., 0.01)
plt.plot(x, runge(x), label = 'Exact function')

orders = [2,5,10,19]

for order in orders:
    xvals = np.linspace(-1.0, 1.0, order + 1)
    interpolant = lagrange(xvals, runge(xvals))
    plt.plot(x, interpolant(x), label=f"order {order}", alpha=0.6)    

plt.ylim(-0.9,1.45)
plt.legend()
plt.show()