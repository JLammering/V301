import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 50, 1000)
plt.plot(a, 0.056169*a/(a**2+2*a*0.196+0.038416))
y, x = np.genfromtxt('V301Daten1.txt', unpack = True)
b = x
x = y/x
y = b*y
plt.plot(x, y, 'k.')
plt.savefig('build/plot5.pdf')
