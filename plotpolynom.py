#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

# Read in the polynomial fit of the random set, used for the final fit.
coeff_last = []
random_coeff = open('/home/nikhilesh/DataTextFiles/used_randoms_set.txt', 'r')
for line in random_coeff:
	coeff_last.append(line)
random_coeff.close()

a_last = float(coeff_last[0])
b_last = float(coeff_last[1])
c_last = float(coeff_last[2])
d_last = float(coeff_last[3])

# Polynomial using the LSQ fit.
coeff_lsq = []
read_in_lsq = open('/home/nikhilesh/DataTextFiles/coeff_lsq.txt', 'r')
for line in read_in_lsq:
	coeff_lsq.append(float(line))
read_in_lsq.close()

a_lsq = coeff_lsq[0]
b_lsq = coeff_lsq[1]
c_lsq = coeff_lsq[2]
d_lsq = coeff_lsq[3]

# Read in the data set.
x = []
y_noise = []
dataset = open('/home/nikhilesh/DataTextFiles/RobinAlgo/c_oben.txt', 'r')
for line in dataset:
	currentline = line.split(" ")
	x.append(currentline[0])
	y_noise.append('-' + currentline[1])
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

# Find the range of the consensus set, as it is useless to extrapolate.
x_min = 1000.0
x_max = -1000.0
for item in x_cons:
	l = float(item)
	if l>x_max:
		x_max = l
	elif l<x_min:
		x_min = l

# Create the x-axis for evaluating the found polynomials.
x_achse = np.linspace(x_min, x_max, 400)

# Sample the polynomial, which fits the random points.
y_last = a_last*x_achse*x_achse*x_achse + b_last*x_achse*x_achse + c_last*x_achse + d_last

# Sample the LSQ fitted polynomial.
y_lsq = a_lsq*x_achse*x_achse*x_achse + b_lsq*x_achse*x_achse + c_lsq*x_achse + d_lsq

# Plot the data.
plt.plot(x, y_noise, 'ro')
plt.plot(x_cons, y_cons, 'bo')
plt.plot(x_achse, y_lsq, 'g')
plt.plot(x_achse, y_last, 'k')
#axes = plt.gca()
#axes.set_xlim([0,800])
#axes.set_ylim([-800,0])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
