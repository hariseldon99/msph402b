#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 18:14:06 2022

Compares the bisection method with the Newton-Raphson method for
solving the equation x^3-37=0.

@author: Analabha Roy
"""
import numpy as np
from scipy.optimize import bisect, newton, ridder
from timeit import Timer

defnum = 100000
x0, x1 = 1.0, 1.25


def func(x):
    return x - (7/5) * np.tanh(x)


def deriv(x):
    return 1 - (7/5) * (1 - np.tanh(x)**2)


mysetup = 'import numpy as np\n'
mysetup += 'from scipy.optimize import bisect, newton, ridder\n'
mysetup += 'x0, x1 = 1.0, 1.25\n'
mysetup += 'def func(x):\
                return x - (7/5) * np.tanh(x)\n'
mysetup += 'def deriv(x):\
                return 1 - (7/5) * (1 - np.tanh(x)**2)'

print("Bisection:")
o = Timer(setup=mysetup, stmt="bisect(func, x0,x1, full_output=True)")
print("Running over a loop of %d" % (defnum))
print("Fastest runtime per execution = ",
      min(o.repeat(number=defnum)) * 1e6 / defnum, " mus")
root, output = bisect(func, x0, x1, full_output=True)
print("Root of equation after %d iterations = %lf" % (output.iterations, root))
print("\n")

print("Newton-Raphson:")
o = Timer(setup=mysetup, stmt="newton(func, x1, fprime=deriv, full_output=True)")
print("Running over a loop of %d" % (defnum))
print("Fastest runtime per execution = ",
      min(o.repeat(number=defnum)) * 1e6 / defnum, " mus")
root, output = newton(func, x1, fprime=deriv, full_output=True)
print("Root of equation after %d iterations = %lf" % (output.iterations, root))
print("\n")

print("Ridders:")
o = Timer(setup=mysetup, stmt="ridder(func, x0,x1, full_output=True)")
print("Running over a loop of %d" % (defnum))
print("Fastest runtime per execution = ",
      min(o.repeat(number=defnum)) * 1e6 / defnum, " mus")
root, output = ridder(func, x0, x1, full_output=True)
print("Root of equation after %d iterations = %lf" % (output.iterations, root))
