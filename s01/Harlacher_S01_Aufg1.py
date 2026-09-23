import numpy as np
import matplotlib.pyplot as plt

def polynomial(x):
    return x**5 - 5*x**4 - 30*x**3 + 110*x**2 + 29*x - 105

def derivative(x):
    return 5*x**4 - 20*x**3 - 90*x**2 + 220*x + 29

def integral(x):
    return x**6/6 - 5*x**5/5 - 30*x**4/4 + 110*x**3/3 + 29*x**2/2 - 105*x

x1 = np.linspace(-10, 11, 1000)
y1 = polynomial(x1)
y2 = derivative(x1)
y3 = integral(x1)


plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x1, y3)
plt.xlim(-10, 10)
plt.ylim(-1500, 1500)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x)')
plt.legend(['y1','y2','y3'])
plt.grid()
plt.show()