#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

# Read in the original parameters of the cubic polynomial.
coeff_orig = []
orig_coeff = open('/home/nikhilesh/DataTextFiles/coeff_orig.txt', 'r')
for line in orig_coeff:
	coeff_orig.append(line)
orig_coeff.close()

a = float(coeff_orig[0])
b = float(coeff_orig[1])
c = float(coeff_orig[2])
d = float(coeff_orig[3])

# Read in the RANSAC parameters of the fitted cubic polynomial.
coeff_lsq = []
read_in_lsq = open('/home/nikhilesh/DataTextFiles/coeff_lsq.txt', 'r')
for line in read_in_lsq:
	coeff_lsq.append(float(line))
read_in_lsq.close()

a_lsq = coeff_lsq[0]
b_lsq = coeff_lsq[1]
c_lsq = coeff_lsq[2]
d_lsq = coeff_lsq[3]

# Read in the noisy data set.
x = []
y_noise = []
dataset = open('/home/nikhilesh/DataTextFiles/data.txt', 'r')
for line in dataset:
	currentline = line.split(" ")
	x.append(currentline[0])
	y_noise.append(currentline[1])
dataset.close()

# Read in the largest consensus set, used for the final LSQ fit.
x_cons = []
y_cons = []
cons_set = open('/home/nikhilesh/DataTextFiles/used_consensus_set.txt', 'r')
for lines in cons_set:
	currentline = lines.split(" ")
	x_cons.append(currentline[0])
	y_cons.append(currentline[1]) # No need to negate. Already done, when reading into cpp program.
cons_set.close()

# Create the x-axis for evaluating the found polynomials.
x_achse = np.linspace(-5.0, 5.0, 500)

# Sample the original polynomial.
y_orig = a*x_achse*x_achse*x_achse + b*x_achse*x_achse + c*x_achse + d

# Sample the LSQ fitted polynomial.
y_lsq = a_lsq*x_achse*x_achse*x_achse + b_lsq*x_achse*x_achse + c_lsq*x_achse + d_lsq

# Plot the data.
plt.plot(x, y_noise, 'ko')
plt.plot(x_cons, y_cons, 'bo')
plt.plot(x_achse, y_lsq, 'b', linewidth=5)
plt.plot(x_achse, y_orig, 'r', linewidth=5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
