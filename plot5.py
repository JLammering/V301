import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

a = np.linspace(0, 50, 1000)
plt.plot(a, 1.96*a/(a**2+2*a*5.1+26.01))
y, x = np.genfromtxt('V301Daten1.txt', unpack = True)

plt.savefig('build/plot5.pdf')
