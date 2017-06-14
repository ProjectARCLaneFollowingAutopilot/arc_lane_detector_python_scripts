#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

# Read in the data set.
f = open('/home/nikhilesh/DataTextFiles/data.txt', 'r')
for line in f:
	currentline = line.split(" ")
	x.append(currentline[0])
	y.append(currentline[1])
f.close()

print(str(len(x))+' '+str(len(y_noise)))


# Plot the data.
plt.plot(x, y, 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
