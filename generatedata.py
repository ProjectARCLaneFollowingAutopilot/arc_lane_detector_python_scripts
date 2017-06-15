#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

# Create a noisy set of data.

'''
# Polynomial of 2nd order.
a = 10
b = 10
c = 10
d = 10
coeff_orig = []
coeff_orig.append(a)
coeff_orig.append(b)
coeff_orig.append(c)
coeff_orig.append(d)

# Write the original parameters to file.
e = open('/home/nikhilesh/DataTextFiles/coeff_orig.txt', 'w')
for i in range(0, len(coeff_orig)):
	e.write(str(coeff_orig[i])+'\n')  # python will convert \n to os.linesep
e.close()  # you can omit in most cases as the destructor will call it
'''

# Create the data set (and add noise).
x = np.linspace(-5.0, 15.0, 200)
y = 2*pow(x-5, 3) + 4*pow(x-5, 2) + (x-5) + 500					#a*x*x*x + b*x*x + c*x + d
noise = np.random.normal(0, 100, 200)
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

