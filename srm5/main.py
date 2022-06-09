import math
def function(x):
    #return x * math.sqrt(81 + x ** 2)
    return 1 / (x ** 2 + 25)


def create_y_list(x_list):
    y_list = []

    for x in x_list:
        y_i = function(x)
        y_list.append(y_i)

    return y_list


def create_x_list(begin, end, h):
    x_list = []

    iterator = begin
    while iterator <= end:
        x_list.append(iterator)
        iterator += h

    return x_list


def trapezoid(y_l, h):
    temp = 0
    for x in range(len(y_l)):
        if x != 0 and x != len(y_l) - 1:
            temp += y_l[x]

    return (h / 2) * (y_l[0] + y_l[len(y_l) - 1] + 2 * temp)


def simpson(y_l, h):
    temp_1 = 0
    temp_2 = 0

    for i in range(len(y_l)):
        if i != 0 and i != len(y_l) - 1:
            if i % 2 != 0:
                temp_1 += y_l[i]
            else:
                temp_2 += y_l[i]
    return (h / 3) * (y_l[0] + y_l[len(y_l) - 1] + 4 * temp_1 + 2 * temp_2)


def rectangle(x_l, h):
    result = 0
    for i in range(len(x_l) - 1):
        result += function((x_l[i] + x_l[i + 1]) / 2) * h

    return result


def runge(result_with_h1, result_with_h2, r):
    return result_with_h2 + abs(result_with_h2 - result_with_h1) / (2 ** r - 1)


def print_result(x_values, y_values, h):
    print(f"FOR h = {h}:")
    print("Rectangle", rectangle(x_values, h))
    print("Trapezoid", trapezoid(y_values, h))
    print("Simpson", simpson(y_values, h))


x_first = -2
x_last = 2
h_1 = 1
h_2 = 0.5

x_values_1 = create_x_list(x_first, x_last, h_1)
y_values_1 = create_y_list(x_values_1)
x_values_2 = create_x_list(x_first, x_last, h_2)
y_values_2 = create_y_list(x_values_2)

print_result(x_values_1, y_values_1, h_1)
print_result(x_values_2, y_values_2, h_2)

print("Runge results:")
print("Rectangle", runge(rectangle(x_values_1, h_1), rectangle(x_values_2, h_2), 2))
print("Trapezoid", runge(trapezoid(y_values_1, h_1), trapezoid(y_values_2, h_2), 2))
print("Simpson", runge(simpson(y_values_1, h_1), simpson(y_values_2, h_2), 4))

# p -> 1 2 4
