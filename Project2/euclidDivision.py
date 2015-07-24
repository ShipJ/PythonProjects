__author__ = 'Jack'

import time


#Euclids algorithm for the greatest common divisor
    # m = int(input("Enter your first integer: "))
    # n = int(input("Enter your second integer: "))

def gcd(m,n):
    x,y,r = m,n,m%n
    if r == 0:
        print("%d is a multiple of %d, %d is your answer." % (m,n,n))
    while r != 0:
        if r == 1:
            print("The answer is 1. Ahh, that means %d and %d are coprime" % (x,y))
            break
        else:
            m = n
            n = r
            r = m % n
        if r == 0:
            print("The greatest common divisor of %d and %d is %d." % (x,y,n))