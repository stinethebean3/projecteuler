#!/bin/python

old1=1
old2=2
current=3

def fib(num):
    while current < 4000000:
        print(current) 
        temp=current
        old2=old1
        old1=current
        current=old1+old2
