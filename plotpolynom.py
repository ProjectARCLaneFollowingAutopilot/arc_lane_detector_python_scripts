#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

# Polynomial of 2nd order.
a = 3
b = 1
c = 4

# Polynomial using the LSQ fit.

a_lsq = 3.89
b_lsq = 1.62
c_lsq = 3.08

# x_achse
x_achse = np.linspace(-2.0, 2.0, 100)

# Create variables to store the original, noisy data set.
x = []
y_noise = []

# Read in the noisy data set.
f = open('/home/nikhilesh/DataTextFiles/data.txt', 'r')
for line in f:
	currentline = line.split(" ")
	x.append(currentline[0])
	y_noise.append(currentline[1])
f.close()

# Sample the original polynomial.
y_orig = a*x_achse*x_achse + b*x_achse + c

# Sample the LSQ fitted polynomial.
y_lsq = a_lsq*x_achse*x_achse + b_lsq*x_achse + c_lsq

# Plot the data.
plt.plot(x, y_noise, 'ro')
plt.plot(x, y_orig, 'b')
plt.plot(x, y_lsq, 'g')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
