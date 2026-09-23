import numpy as np

#Polynom
def polynomial(vector, x):
    p = 0

    for i in range(vector.size):
        power = vector.size - 1 - i
        p += vector.flat[i] * x**power

    return p


#Ableitung
def derivative(vector, x):
    dp = 0
    n = vector.size - 1

    for i in range(vector.size - 1):
        power = n - i
        dp += vector.flat[i] * power * x**(power - 1)

    return dp

#Stammfunktion
def integral(vector, x):
    pint = 0
    n = vector.size - 1

    for i in range(vector.size):
        power = n - i
        pint += vector.flat[i] / (power + 1) * x**(power + 1)

    return pint


def Harlacher_S01_Aufg2(a, xmin, xmax):
    a = np.array(a)
    shape = np.shape(a)

    if shape == (0,):
        raise ValueError("Input vector cannot be empty")

    if len(shape) != 2 or (shape[0] != 1 and shape[1] != 1):
        raise ValueError("a must be a row or column vector")

    x = np.linspace(xmin, xmax, 1000)

    p = polynomial(a, x)
    dp = derivative(a, x)
    pint = integral(a, x)

    return x, p, dp, pint