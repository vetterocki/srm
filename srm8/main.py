import numpy as np
from scipy.optimize import fsolve


class NonLinearSystemSolver:
    def __init__(self, x_values, epsilon):
        self.__x_values = x_values
        self.__epsilon = epsilon
        self.__result = []

    @property
    def x_values(self):
        return self.__x_values

    @property
    def epsilon(self):
        return self.__epsilon

    @epsilon.setter
    def epsilon(self, epsilon):
        self.__epsilon = epsilon

    @x_values.setter
    def x_values(self, x_values):
        self.__x_values = x_values

    @staticmethod
    def function(variables):
        x_1, x_2 = variables

        return [x_1 - np.cos(x_2) - 1,
                x_2 - np.log10(x_1 + 7) - 10]

    @staticmethod
    def jacobian_matrix(variables):
        x_1, x_2 = variables
        return [[1, np.sin(x_2)],
                [(-1 / (np.log(10) * (x_1 + 1))), 1]]


class Newton(NonLinearSystemSolver):
    def __init__(self, x_values, epsilon):
        super(Newton, self).__init__(x_values, epsilon)

    def newton(self, funct=NonLinearSystemSolver.function, jacobian=NonLinearSystemSolver.jacobian_matrix):
        x_last = self.x_values

        for k in range(50):

            jacob = np.array(jacobian(x_last))
            func = np.array(funct(x_last))

            diff = np.linalg.solve(jacob, -func)
            x_last = x_last + diff
            self.__result = x_last

            if np.linalg.norm(diff) < self.epsilon:
                break

        return list(self.__result)


class SimpleIteration(NonLinearSystemSolver):
    def __init__(self, x_values, epsilon):
        super(SimpleIteration, self).__init__(x_values, epsilon)

    @staticmethod
    def function_for_iter(x_1, x_2):
        return x_1 - np.cos(x_2) - 1

    @staticmethod
    def f_1_for_iter(x1, x_2):
        return 1 + np.cos(x_2)

    @staticmethod
    def f_2_for_iter(x_1, x2):
        return 10 + np.log10(x_1 + 7)

    def simple_iteration(self):
        x1 = self.x_values[0]
        x2 = self.x_values[1]
        while abs(self.function_for_iter(x1, x2)) > self.epsilon:
            x1, x2 = self.f_1_for_iter(x1, x2), self.f_2_for_iter(x1, x2)
            self.__result = [x1, x2]

        return self.__result


x = [0, 1]

checker = fsolve(NonLinearSystemSolver.function, x, fprime=NonLinearSystemSolver.jacobian_matrix, full_output=1)
print("Scipy перевірка:", list(checker[0]))

newton = Newton(x, 10e-4)
print("Метод Ньютона:", newton.newton())

simple = SimpleIteration(x, 10e-4)
print("Метод простих ітерацій:", simple.simple_iteration())
