import numpy as np

def y_1(x):
    return 1 - 0.1 * x


def y_2(x):
    return -2.04


def y_3(x):
    return 1 + 0.1 * x


x_list = [0.2, 0.4, 0.6, 0.8]
list_for_matrix = np.zeros((5, 5))


def generate_values(matrix):
    j = 0
    for i in range(len(matrix) - 1):
        if i != 0:
            matrix[i][j] = y_2(x_list[i])
            matrix[i][j - 1] = y_1(x_list[i])
            matrix[i][j + 1] = y_3(x_list[i])
        elif i == 0 and j == 0:
            matrix[i][j] = y_2(x_list[i])
            matrix[i][j + 1] = y_3(x_list[i])

        j += 1


generate_values(list_for_matrix)
list_for_matrix[len(list_for_matrix) - 1] = [0, 0, 0, 1, -1.4]
print(list_for_matrix)
d = np.array([0.98, 0, 0, 0, 0])
print(abs((np.linalg.solve(list_for_matrix, d))))
