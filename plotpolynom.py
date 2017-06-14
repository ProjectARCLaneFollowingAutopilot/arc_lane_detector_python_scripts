#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

# Polynomial of 2nd order.
# Read in the original parameters.
coeff_orig = []
e = open('/home/nikhilesh/DataTextFiles/coeff_orig.txt', 'r')
for line in e:
	coeff_orig.append(float(line))
e.close()

a = coeff_orig[0]
b = coeff_orig[1]
c = coeff_orig[2]
d = coeff_orig[3]

# Polynomial using the LSQ fit.
# Read in the found parameters.
coeff_lsq = []
g = open('/home/nikhilesh/DataTextFiles/coeff_lsq.txt', 'r')
for line in g:
	coeff_lsq.append(float(line))
g.close()

a_lsq = coeff_lsq[0]
b_lsq = coeff_lsq[1]
c_lsq = coeff_lsq[2]
d_lsq = coeff_lsq[3]

# x_achse
x_achse = np.linspace(-2.0, 2.0, 200)

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

print(str(len(x))+' '+str(len(y_noise)))


# Sample the original polynomial.
y_orig = a*x_achse*x_achse*x_achse + b*x_achse*x_achse + c*x_achse + d

# Sample the LSQ fitted polynomial.
y_lsq = a_lsq*x_achse*x_achse*x_achse + b_lsq*x_achse*x_achse + c_lsq*x_achse + d_lsq

# Plot the data.
plt.plot(x, y_noise, 'ro')
plt.plot(x_achse, y_orig, 'b')
plt.plot(x_achse, y_lsq, 'g')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
