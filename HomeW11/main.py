import matplotlib.pyplot as plt
import numpy as np
import pylab

plt.style.use('bmh')

x = np.linspace(-11, 11, 100)

pylab.subplot(2, 1, 1)

a = x**3
b = x * 50
y = a - b
pylab.plot(x, y);

c = x**4
c = c * -1
d = x**2
d = d * 88
y = c + d
y = y - 241
pylab.plot(x, y);

pylab.subplot(2, 1, 2)

y = a + b
y = y - c
y = y - d
y = y + 241
pylab.plot(x, y);

pylab.show()