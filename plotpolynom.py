#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

# Polynomial of 2nd order.
a = 3
b = 1
c = 4

# Polynomial using the LSQ fit.
'''
a_lsq = 
b_lsq = 
c_lsq = 
'''
x = []
y_noise = []
y_noise

# Read in the noisy data set.
f = open('/home/nikhilesh/DataTextFiles/data.txt', 'r')
for line in f:
	currentline = line.split(" ")
	x.append(currentline[0])
	y_noise.append(currentline[1])
f.close()

# Plot the data.
plt.plot(x, y_noise, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
