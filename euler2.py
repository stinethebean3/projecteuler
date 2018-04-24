#!/bin/python

current=2
old1=1
old2=0
out=0

while current < 4000000:
    if current % 2 == 0:
        out = out + current 
    old2=old1
    old1=current
    current=old1+old2
print(out) 
