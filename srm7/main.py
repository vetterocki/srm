import numpy as np


def gauss(matrix):
    result = np.zeros(len(matrix))
    loop_range = len(matrix)

    for i in range(loop_range):
        if matrix[i][i] == 0:
            raise Exception("Invalid arguments -> division by zero!")

        for j in range(loop_range):
            if i != j:
                division = matrix[j][i] / matrix[i][i]

                for y in range(loop_range + 1):
                    matrix[j][y] = matrix[j][y] - division * matrix[i][y]

    for x in range(loop_range):
        result[x] = matrix[x][loop_range] / matrix[x][x]

    return result


def gauss_seidel(a_matrix, b_matrix, max_iterations, x_values):
    for j in range(max_iterations):

        x_old = x_values.copy()

        for j in range(a_matrix.shape[0]):
            x_values[j] = (b_matrix[j] - np.dot(a_matrix[j, :j], x_values[:j]) -
                           np.dot(a_matrix[j, (j + 1):], x_old[(j + 1):])) / a_matrix[j, j]

    return x_values


def print_gauss(matrix):
    result = gauss(matrix)

    for i in result:
        print(f"{i:.{3}f}", end=" ")
    print()


m = [[-2, -9, -3, 7, -26],
     [-7, 8, 2, 5, -25],
     [-6, 2, 0, 0, -16],
     [0, -3, 8, -3, -5]]

a = np.array([[-24, -6, 4, 7],
              [-8, 21, 4, -2],
              [6, 6, 16, 0],
              [-7, -7, 5, 24]])

b = np.array([130, 139, -84, -165])
x = np.array([0, 0, 0, 0])

print_gauss(m)
print(gauss_seidel(a, b, 2, x))
