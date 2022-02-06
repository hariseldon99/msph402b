#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 00:33:01 2022

@author: Analabha Roy
"""
import numpy as np
from scipy.interpolate import lagrange

t_eval = 16.0
t = np.array([0, 10, 15, 20, 22.5, 30])
v_t = np.array([0, 227.04, 362.78, 517.35, 602.97, 901.67])

interpolant = lagrange(t[1:5], v_t[1:5])
interp_val = np.polyval(interpolant, t_eval)

t0, t1 = 11, 16
s = np.polyint(interpolant)

print('The distance travelled in the time interval', t0, '-' , t1, '=', 
	np.polyval(s, t1)-np.polyval(s, t0))
print('The value of the interpolant of order', interpolant.order, 'at t =',
      t_eval, 'is', interp_val)
print("Interpolant:")
print(interpolant)
