#!/usr/bin/env python3
N = 53
eps = 1.0
for i in range(N):
    eps = eps /2
    onepeps = 1.0 + eps
    print('eps = ', eps, ' , one + eps = ', onepeps)
