#!/bin/python

target = 600851475143
factor = 0

for x in range(3, int(target ** 0.5) + 1, 2):
    if (target % x == 0):
        isPrime=True
        for y in range(2, x):
            if x % y == 0:
                isPrime=False
                break
        if isPrime == True:
            factor = x
print(factor)
        

