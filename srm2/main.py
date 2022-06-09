import numpy as np
import matplotlib.pyplot as plt
from math import fabs


def draw_graph():
    x = np.arange(-2, 2, 0.01)
    plt.plot(x, x ** 3 + x ** 2, x, x + 1.5)
    plt.show()


print("Подивіться на графік та визначте приблизнйи інтервал кореня", draw_graph())

a_inp = float(input("Введіть початок інтервалу:"))
b_inp = float(input("Введіть кінець інтервалу:"))
eps_inp = float(input("Введіть необхідну точність:"))


def function(x):
    return x ** 3 + x ** 2 - x - 1.5


def bisection_method(a, b, eps):
    print("Метод половинного ділення:")

    counter = 0
    c = 0

    while b - a > eps:
        c = (a + b) / 2.0
        if function(b) * function(c) < 0:
            a = c
        else:
            b = c

        print(f'{counter} {a:.{4}f} {b:.{4}f} {function(a) :.{4}f} {function(b) :.{4}f} {c:.{4}f} {function(c) :.{4}f}')
        counter += 1

    print(f'Корінь ≈ {c:.{4}f}')


def chord_method(a, b, eps):
    print("Метод хорд:")

    def x(a, b):
        return a - function(a) * (b - a) / (function(b) - function(a))

    counter = 0

    if function(a) * function(x(a, b)) <= 0:
        b = x(a, b)
    else:
        a = x(a, b)

    while fabs(function(x(a, b))) > eps:
        if function(a) * function(x(a, b)) <= 0:
            b = x(a, b)
        else:
            a = x(a, b)

        print(
            f'{counter} {a:.{4}f} {b:.{4}f} {function(a) :.{4}f} '
            f'{function(b) :.{4}f} {x(a, b):.{4}f} {function(x(a, b)) :.{4}f}')
        counter += 1
    print(f'Корінь ≈ {x(a, b):.{4}f}')


def diff_function(x):
    return 3 * x ** 2 + 2 * x - 1


def diff_function_max(b):
    return diff_function(b)


def newton_method(a, b, eps):
    print("Метод Ньютона:")

    counter = 0

    x_f = (a + b) / 2
    x = function(x_f)
    x_n = x - function(x) / diff_function(x)

    while fabs(x_n - x) > eps:
        x = x_n
        x_n = x - function(x) / diff_function(x)

        print(f'{counter} {x_n:.{4}f} {function(x_n) :.{4}f} {diff_function(x_n) :.{4}f} '
              f'{(-function(x_n) / diff_function(x_n)):.{4}f}')
        counter += 1
    print(f'Корінь ≈ {x_n:.{4}f}')


def iteration_func(x, b):
    return x - 1 / diff_function_max(b) * (x ** 3 + x ** 2 - x - 1.5)


def simple_iteration_method(a, b, eps):
    print("Метод простої ітерації:")

    counter = 0
    x = (a + b) / 2
    temp = x
    x = iteration_func(x, b)

    while fabs(x - temp) >= eps:
        temp = x
        x = iteration_func(x, b)

        print(f'{counter} {temp:.{4}f} {x:.{4}f}')
        counter += 1
    print(f'Корінь ≈ {temp:.{4}f}')


bisection_method(a_inp, b_inp, eps_inp)
chord_method(a_inp, b_inp, eps_inp)
newton_method(a_inp, b_inp, eps_inp)
simple_iteration_method(a_inp, b_inp, eps_inp)
