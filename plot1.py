# V301
# Graph von Uk in Abhägigkeit von I (Aufgabe b, einfache Klemmenspannung)
# Lineare Regression: Angabe von Steigung, Abschnitt und Fehler
# Messwerte aus der Datei 'V301Daten1.txt'

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Messwerte:
y, x = np.genfromtxt('V301Daten1.txt', unpack = True)

# Fehlerbalken:
errX = (0.03, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003)
plt.errorbar(x, y, xerr = errX, yerr = 0.06, fmt = 'kx', label = r'$Messwerte \, und \, Fehlerbalken$')

# Lineare Regression:
slope, intercept, r_value, p_value, std_err = linregress(x, y)
a = np.linspace(0.02, 0.15)
plt.plot(a, slope*a + intercept, 'r-', label = r'$linregress$')

# Ausgabe:
print(linregress(y, x))

plt.legend(loc = 'best')
plt.xlim(0.02, 0.15)
plt.xlabel(r'$(I/\mathrm{A})$')
plt.ylabel(r'$(U_k/\mathrm{V})$')
plt.grid()

plt.savefig('plot1.pdf')
