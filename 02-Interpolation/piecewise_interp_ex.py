#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 16:34:55 2022

@author: Analabha Roy
"""
import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

t = np.linspace(0, np.pi, 5)
v_t = np.sin(t)

size = 3
step = 2

t_pieces = [t[i:i + size] for i in range(0, len(t), step)]
vt_pieces = [v_t[i:i + size] for i in range(0, len(v_t), step)]

for n, tpiece in enumerate(t_pieces):
    interpolant = lagrange(tpiece, vt_pieces[n])
    t_cont = np.linspace(tpiece[0], tpiece[-1], 1000)
    interp_vals = interpolant(t_cont)
    plt.plot(t_cont, interp_vals, 'r--')

full_interpolant = lagrange(t, v_t)
interp_vals = full_interpolant(t)
plt.scatter(t, interp_vals, alpha=0.5)

t_cont = np.linspace(0, np.pi, 1000)
plt.plot(t_cont, np.sin(t_cont), alpha=0.5)

plt.show()
