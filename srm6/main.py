import math


def function(x, y):
    return (x * (math.e ** x) + y) / (x + 1)


def real_function(x):
    return x + 1 + math.e ** x


def euler(x, y, h, n):
    for i in range(1, n + 1):
        func = function(x, y)
        y += func * h
        x += h
        epsilon = abs((real_function(x)) - y)
        print(f"x = {x:.{5}f} y = {y:.{5}f} accurate = {real_function(x):.{5}f} epsilon = {epsilon}")


def euler_cauchy(x, y, h, n):
    y_1 = y
    for i in range(1, n + 1):
        func = function(x, y)
        x += h

        y += 0.5 * h * (func + function(x, y_1 + h * func))
        epsilon = abs(real_function(x) - y)
        print(f"x = {x:.{5}f} y = {y:.{5}f} accurate = {real_function(x):.{5}f} epsilon = {epsilon}")
        y_1 = y


def runge_kutta(x0, y0, h, n):
    epsilon = abs((x0 + 1 + math.e ** x0) - y0)

    for i in range(1, n + 1):
        k1 = h * (function(x0, y0))
        k2 = h * (function((x0 + h / 2), (y0 + k1 / 2)))
        k3 = h * (function((x0 + h / 2), (y0 + k2 / 2)))
        k4 = h * (function((x0 + h), (y0 + k3)))
        k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        yn = y0 + k
        epsilon = abs(real_function(x0) - y0)
        print(f"x = {x0:.{5}f} y = {y0:.{5}f} accurate = {real_function(x0):.{5}f} epsilon = {epsilon}")

        y0 = yn
        x0 = x0 + h

    print(f"x = {x0:.{5}f} y = {y0:.{5}f} accurate = {real_function(x0):.{5}f} epsilon = {epsilon}")


print("Метод Ейлера")
euler(1, 2 + math.e, 0.1, 10)
print("Метод Ейлера-Коші")
euler_cauchy(1, 2 + math.e, 0.1, 10)
print("Метод Рунге-Кутта 4 порядку")
runge_kutta(1, 2 + math.e, 0.1, 10)
