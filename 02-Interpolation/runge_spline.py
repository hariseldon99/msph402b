#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 16:00:47 2022

@author: Analabha Roy
"""

import numpy as np
from scipy.interpolate import lagrange, interp1d
import matplotlib.pyplot as plt

def runge(x):
    return 1/(1 + 25 * x**2)

x = np.arange(-1., 1., 0.01)
plt.plot(x, runge(x), 'r--', label='Exact function', alpha=0.5)

npoints = 8

xvals = np.linspace(-1.0, 1.0, npoints + 1)
interpolant = lagrange(xvals, runge(xvals))
plt.plot(x, np.polyval(interpolant, x), label="Langrange: order %d"
         % (npoints), alpha=0.5)
plt.scatter(xvals, np.polyval(interpolant, xvals), alpha=0.5)

spline = interp1d(xvals, runge(xvals), kind='cubic')
plt.plot(x, spline(x), label="Cubic Spline")

plt.ylim(-1.1, 1.45)
plt.legend()
plt.show()
