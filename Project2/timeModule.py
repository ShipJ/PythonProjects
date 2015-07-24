__author__ = 'Jack'

#This is an example of how to use the time function to measure how long a function takes to perform

import time
from euclidDivision import gcd #from another file with the GCD function, I can use it in this one

start_time = time.time() #timer starts
gcd(235423,2434) #function operates
print("-- The process took %s seconds --" % (time.time() - start_time)) #function ends, time now - time at start