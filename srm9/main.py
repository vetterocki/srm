import numpy as np

y_k_left = lambda x: 1.06
y_k_middle = lambda x: -2 - 0.04 * x
y_k_right = lambda x: 0.94


class LinearSystemGenerator:
    def __init__(self, row, column, step, first, last):
        self.__initial_matrix = np.zeros((row, column))
        self.__step = step
        self.__first = first
        self.__last = last

    @property
    def initial_matrix(self):
        return self.__initial_matrix

    @property
    def first(self):
        return self.__first

    @property
    def last(self):
        return self.__last

    @property
    def step(self):
        return self.__step

    @first.setter
    def first(self, first):
        self.__first = first

    @last.setter
    def last(self, last):
        self.__last = last

    @initial_matrix.setter
    def initial_matrix(self, row, number):
        self.validate([row, number])
        self.__initial_matrix = np.zeros((row, number))

    @step.setter
    def step(self, step):
        self.validate(step)
        self.__step = step

    @staticmethod
    def validate(value):
        for elem in value:
            if elem <= 0:
                raise Exception("value can not be equal or less than 0!")

    def get_steps(self):
        iterator = self.first
        iterations = (self.last - self.first) / self.step
        counter = 1
        steps = []

        while not counter == iterations:
            iterator += self.step
            steps.append(iterator)
            counter += 1

        return steps

    def generate_les(self):
        column = 0
        matrix = self.__initial_matrix

        for row in range(0, len(matrix)):
            current_step = self.get_steps()[row - 1]
            if row != 0 and column != 4:
                matrix[row][column] = y_k_middle(current_step)
                matrix[row][column - 1] = y_k_left(current_step)
                matrix[row][column + 1] = y_k_right(current_step)
            elif column == 4:
                matrix[row][column] = y_k_middle(current_step)
                matrix[row][column - 1] = y_k_left(current_step)

            column += 1

        self.__initial_matrix = matrix

    def fill_special_row(self, values, index):
        self.__initial_matrix[index] = values


class LinearSystemSolver(LinearSystemGenerator):
    def __init__(self, row, column, step, first, last, d_row):
        super(LinearSystemSolver, self).__init__(row, column, step, first, last)
        self.__d_row = d_row

    @property
    def d_row(self):
        return self.__d_row

    @d_row.setter
    def d_row(self, d_row):
        self.validate(d_row)
        self.__d_row = d_row

    def solve_les(self):
        return np.linalg.solve(self.initial_matrix, self.__d_row)


try:
    solver = LinearSystemSolver(5, 5, 0.2, 1.9, 2.9, [0.018, 0.048, 0.048, 0.0480, -1.822])
    solver.generate_les()
    solver.fill_special_row([1.36, -1, 0, 0, 0], 0)
    print("Трьохдіагональна система (СЛАР):")
    print(solver.initial_matrix)
    print("Розв'язок СЛАР:", solver.solve_les())

except Exception as exception:
    print(exception)
