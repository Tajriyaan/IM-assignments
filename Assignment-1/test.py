import matplotlib.pyplot as plt
from math import log
import numpy as np

k=4

x = np.linspace(1,7)
y1 = np.log2(x)
y2 = [(xi) for xi in x]
y3 = [(xi**2) for xi in x]
y4 = [(xi**3) for xi in x]
y5 = [(xi**k)for xi in x]


plt.figure(figsize=(6,4))
plt.title("Graphs for f(n)")
plt.xlabel("n")
plt.ylabel("f(n)")


plt.plot(x, y1, label='log(n)')
plt.plot(x, y2,  label='n')
plt.plot(x, y3,  label='log(n^2)')
plt.plot(x, y4,  label='log(n^3)')
plt.plot(x, y5,  label='n^k')
plt.grid()
plt.legend()

plt.show()

