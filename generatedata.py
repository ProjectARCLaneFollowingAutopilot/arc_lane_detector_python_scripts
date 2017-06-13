#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

# Create a noisy set of data.

# Polynomial of 2nd order.
a = 3
b = 1
c = 4

# Create the data set (and add noise).
x = np.linspace(-2.0, 2.0, 100)
y = a*x*x + b*x + c
noise = np.random.normal(0, 3, 100)
y_noise = y + noise

# Write x, y(x) directly to file.
f = open('/home/nikhilesh/DataTextFiles/data.txt', 'w')
for i in range(0, len(x)):
	f.write(str(x[i])+' '+str(y_noise[i])+'\n')  # python will convert \n to os.linesep

f.close()  # you can omit in most cases as the destructor will call it

# Plot the data.
plt.plot(x, y_noise, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

