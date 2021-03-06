# V301
# Graph von Uk in Abhägigkeit von I (Aufgabe d, RC-Generator, Rechteck)
# Lineare Regression: Angabe von Steigung, Abschnitt und Fehler
# Messwerte aus der Datei 'V301Daten3a.txt'

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Messwerte:
y, x = np.genfromtxt('V301Daten3a.txt', unpack = True)

# Fehlerbalken:
plt.errorbar(x, y, xerr = 0.3, yerr = 0.03, fmt = 'kx', label = r'$Messwerte \, und \, Fehlerbalken$')

# Lineare Regression:
slope, intercept, r_value, p_value, std_err = linregress(x, y)
a = np.linspace(1.5, 7)
plt.plot(a, slope*a + intercept, 'r-', label = r'$Ausgleichsgerade$')

# Ausgabe:
print(linregress(x, y))

plt.legend(loc = 'best')
plt.xlim(1.5, 7)
plt.xlabel(r'$(I/\mathrm{mA})$')
plt.ylabel(r'$(U_k/\mathrm{V})$')
plt.grid()

plt.savefig('build/plot3a.pdf')
