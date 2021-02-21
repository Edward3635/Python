import math
import matplotlib.pyplot as plt
import numpy as np


def Function(x):
    return math.log(2 * x + 1) - (x) ** 3 + 1


def Derivative(x):
    return (2 / (2 * x + 1)) - 3 * x ** 2


def FunctionRemake(x):
    return np.e ** (x ** 3 - 1) / 2 - 0.5


def FunctionRemake2(x):
    return (math.log(2 * x + 1) + 1) ** (1 / 3)


a, b = -0.49, 0.0
a1, b1 = 1.0, 1.5

e = 0.001


def PolDilMethod(function, a, b):
    while abs(b - a) > e:
        x = (a + b) / 2.0
        if (function(x) < 0 and function(a) < 0) or (function(x) > 0 and function(a) > 0):
            a = x
        else:
            b = x
    return x


def NewtonsMethod(function, derivative, x):
    x1 = x - function(x) / derivative(x)
    while abs(function(x1) - function(x)) > e:
        x = x1
        x1 = x - function(x) / derivative(x)
    return x1


def DeleteMe(function, derivative, a, b):
    x = (a + b) / 2.0
    x1 = x - function(x) / derivative(x)
    while abs(function(x1) - function(x)) > e:
        x = x1
        x1 = x - function(x) / derivative(x)
    return x1


def SimpleIterationMethod(remake, a, b):
    x0 = (a + b) / 2.0
    x, x1 = x0, remake(x0)
    while abs(x - x1) > e:
        x = x1
        x1 = remake(x)
    return x1


v1, v2, v3 = "Корінь рівняння методом половинного ділення:", "Корінь рівняння методом Ньютона:", \
             "Корінь рівняння методом ітерацій:"
line = " |———————————————————————————————————————————————————————————|"
print(line)
print("|", v1, PolDilMethod(Function, a, b), "|")
print("|", v1, PolDilMethod(Function, a1, b1), "  |")
print(line)
print("|", v2, NewtonsMethod(Function, Derivative, -0.49), "        |")
print("|", v2, NewtonsMethod(Function, Derivative, 1.5), "        |")
print(line)
print("|", v3, SimpleIterationMethod(FunctionRemake, a, b), "      |")
print("|", v3, SimpleIterationMethod(FunctionRemake2, a1, b1), "        |")
print(line)
print("Метод Ньютона апгрейд %s" % DeleteMe(Function, Derivative, a, b))
print("Метод Ньютона апгрейд %s" % DeleteMe(Function, Derivative, a1, b1))

x1 = np.arange(-0.48, 1.5, 0.001)
y1 = np.log(2 * (np.power(x1, 1)) + 1)

x2 = np.arange(-1.0, 1.5, 0.001)
y2 = np.power(x2, 3) - 1

fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.plot(x2, y2)
ax.set(xlabel='x', ylabel='y')
ax.grid()
plt.show()
