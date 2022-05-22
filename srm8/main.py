import numpy as np
from scipy.optimize import fsolve


def function(variables):
    x_1, x_2 = variables

    return [x_1 - np.cos(x_2) - 1,
            x_2 - np.log10(x_1 + 7) - 10]


def jacobian_matrix(variables):
    x_1, x_2 = variables
    return [[1, np.sin(x_2)],
            [(-1 / (np.log(10) * (x_1 + 1))), 1]]


def newton(funct, x_values, jacobian, epsilon):
    x_last = x_values

    for k in range(50):

        jacob = np.array(jacobian(x_last))
        func = np.array(funct(x_last))

        diff = np.linalg.solve(jacob, -func)
        x_last = x_last + diff

        if np.linalg.norm(diff) < epsilon:
            break

    return x_last


def function_for_iter(x_1, x_2):
    return x_1 - np.cos(x_2) - 1


def f_1_for_iter(x1, x_2):
    return 1 + np.cos(x_2)


def f_2_for_iter(x_1, x2):
    return 10 + np.log10(x_1 + 7)


def simple_iteration(x1, x2, eps=.001):
    while abs(function_for_iter(x1, x2)) > eps:
        x1, x2 = f_1_for_iter(x1, x2), f_2_for_iter(x1, x2)

    return x1, x2


def iter_(x1, x2):
    x1, x2 = simple_iteration(x1, x2)

    return [x1, x2]


x0 = [0, 1]
cheat = fsolve(function, x0, fprime=jacobian_matrix, full_output=1)
norm = newton(function, x0, jacobian_matrix, 10 ** -4)
iteration = simple_iteration(0, 1, 10 ** -4)
print("Перевірка:", cheat)
print("Методом Ньютона:", norm)
print("Методом простих ітерацій:", iteration)
