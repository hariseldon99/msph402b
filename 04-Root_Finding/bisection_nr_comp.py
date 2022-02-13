#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 18:14:06 2022

Compares the bisection method with the Newton-Raphson method for
solving the equation x^3-37=0.

@author: Analabha Roy
"""
from scipy.optimize import bisect, newton
from timeit import Timer

defnum = 100000

x0, x1 = 2.0, 5.0

mysetup = 'from scipy.optimize import bisect, newton; x0, x1 = 2.0, 5.0'

print("Bisection:")
o = Timer(setup=mysetup,
          stmt="bisect(lambda x: x**3 - 37, x0,x1, full_output=True)")
print("Running over a loop of %d" % (defnum))
print("Fastest runtime per execution = ",
      min(o.repeat(number=defnum)) * 1e6 / defnum, " mus")
root, output = bisect(lambda x: x**3 - 37, x0, x1, full_output=True)
print("Root of equation after %d bisections = %lf\n" % (output.iterations,
                                                        root))

print("Newton-Raphson:")
o = Timer(setup=mysetup, stmt="newton(lambda x: x**3 - 37, x1,\
                          fprime=lambda x: 3 * x**2, full_output=True)")
print("Running over a loop of %d" % (defnum))
print("Fastest runtime per execution = ",
      min(o.repeat(number=defnum)) * 1e6 / defnum, " mus")
root, output = newton(lambda x: x**3 - 37, x1, fprime=lambda x: 3 * x**2,
                      full_output=True)
print("Root of equation after %d iterations = %lf" % (output.iterations, root))
