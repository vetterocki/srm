import math

import numpy as np
import matplotlib.pyplot as plt


a = 5
b = 4


def task_1(a, b):
    s = a * b
    p = 2 * (a + b)
    return s, p


print(task_1(a, b))
a = 5
b = 4


def task_2(a, b):
    return math.sqrt(a * b)


print(task_2(a, b))

x_1 = 2
y_1 = 6
x_2 = 10
y_2 = 13


def task_3(x_1, y_1, x_2, y_2):
    s = (x_2 - x_1) * (y_2 - y_1)
    p = 2 * ((x_2 - x_1) + (y_2 - y_1))
    return s, p


print(task_3(x_1, y_1, x_2, y_2))
a = 5
b = 4


def task_4(a):
    if (a % 2 == 0):
        return True
    else:
        return False


print(task_4(a))
print(task_4(b))

a = 5
b = 4
c = 3


def task_5(a, b, c):
    return a < b < c, a > 0 or b > 0 or c > 0, (a > 0 and (b < 0 and c < 0) or
                                                b > 0 and (a < 0 and c < 0) or c > 0 and (a < 0 and b < 0))


print(task_5(a, b, c))


def task_6():
    matrix_random = np.random.rand(50, 50)
    tr_matrix = matrix_random.transpose()
    min_avg = 0
    max_dev = 0
    for i in range(len(tr_matrix)):
        avg = np.average(tr_matrix[i])
        if np.average(tr_matrix[min_avg]) > avg:
            min_avg = i

        dev = np.std(tr_matrix[i])
        if np.std(tr_matrix[max_dev]) < dev:
            max_dev = i

    plt.title("Graph ")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(tr_matrix[min_avg], tr_matrix[max_dev], "y")
    plt.show()


print(task_6())

x_1 = 2
y_1 = 2
x_2 = 4
y_2 = 6


def task_8(x_1, y_1, x_2, y_2):
    if (y_2 != y_1 and x_2 != x_1):
        if (x_1 == y_1 and x_2 == y_2):
            return True
        else:
            return False
    else:
        return True


print(task_8(x_1, y_1, x_2, y_2))

a = 4
b = 8


def task_9(a, b):
    counter = 0
    result = []
    if (a < b):
        for i in range(a, b + 1, 1):
            counter += 1
            result.append(i)

        return result, counter
    else:
        return "a > b!"


print(task_9(a, b))

a = 2456


def task_10(a):
    temp = 0
    while a > 0:
        last_n = a % 10
        a = a // 10
        temp = temp * 10
        temp = temp + last_n
    return temp


print(task_10(a))

array = [1, 7, 4, 5]


def task_11(array):
    sr = np.mean(array)
    for i in range(len(array)):
        if (array[i] > sr):
            array[i] -= 18
    return array


print(task_11(array))

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def task_12(matrix):
    tr_matrix = matrix.transpose()
    for j in tr_matrix:
        plt.hist(j)
        plt.show()


print(task_12(matrix))
a = 13


def task_13(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False


print(task_13(a))
x = 1
y = 3


def task_7(x, y):
    if ((x and y % 2 == 0) or (x and y % 2 != 0)):
        return False
    else:
        return True


print(task_7(x, y))

_str = "Hello"
str_ = _str + str(10)
print(str_)
