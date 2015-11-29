import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

# Leistungskurve N(R_A):
a = np.linspace(0, 50, 1000)
plt.plot(a, 1.96*a/(a**2+2*a*5.1+26.01), label = r'$Leistungskurve \, N(R_A)$')

# Messwerte mit uncertainties:
# errX = (0.03, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003)
# y, x = np.genfromtxt('V301Daten1.txt', unpack = True)

# m = unp.uarray(x, errX)
# n = unp.uarray(y, 0.06)

# print(n*m)
# print(u*v)

# Messwerte mit Fehlerbalken:

y, x = np.genfromtxt('V301Daten1.txt', unpack = True)
u = y
y = x * y
x = u/x
errX = (1, 0.8, 1, 2, 2, 3, 4, 5, 5)
errY = (0.02, 0.006, 0.005, 0.005, 0.004, 0.004, 0.004, 0.004, 0.004)
plt.errorbar(x, y, xerr = errX, yerr = errY, fmt = 'kx', label = r'$Messwerte \, und \, Fehlerbalken$')

plt.legend(loc = 'best')
plt.grid()

plt.savefig('build/plot5.pdf')
