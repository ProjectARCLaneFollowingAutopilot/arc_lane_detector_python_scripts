#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

'''
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
'''
# Read in last sample.

coeff_last = []
p = open('/home/nikhilesh/DataTextFiles/used_randoms_set.txt', 'r')
for line in p:
	coeff_last.append(line)
p.close()

a_last = float(coeff_last[0])
b_last = float(coeff_last[1])
c_last = float(coeff_last[2])
d_last = float(coeff_last[3])

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

# Create variables to store the original, noisy data set.
x = []
y_noise = []

# Read in the noisy data set.
f = open('/home/nikhilesh/DataTextFiles/RobinAlgo/c_oben.txt', 'r')
for line in f:
	currentline = line.split(" ")
	x.append(currentline[0])
	y_noise.append('-' + currentline[1])
f.close()

# Read in the largest consensus set. /home/nikhilesh/DataTextFiles/used_consensus_Set.txt
x_cons = []
y_cons = []
q = open('/home/nikhilesh/DataTextFiles/used_consensus_set.txt', 'r')
for lines in q:
	currentline = lines.split(" ")
	x_cons.append(currentline[0])
	y_cons.append(currentline[1]) # No need to negate. Already done, when reading into cpp program.
q.close()

x_min = 1000.0
x_max = -1000.0
for item in x_cons:
	l = float(item)
	if l>x_max:
		x_max = l
	elif l<x_min:
		x_min = l

# x_achse
x_achse = np.linspace(x_min, x_max, 400)

# Sample the original polynomial.
#y_orig = a*x_achse*x_achse*x_achse + b*x_achse*x_achse + c*x_achse + d

# Sample the LSQ fitted polynomial.
y_lsq = a_lsq*x_achse*x_achse*x_achse + b_lsq*x_achse*x_achse + c_lsq*x_achse + d_lsq
y_last = a_last*x_achse*x_achse*x_achse + b_last*x_achse*x_achse + c_last*x_achse + d_last

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
