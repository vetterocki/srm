from scipy import interpolate

x = -0.5
q = [0, 1.61, -0.404, 14.115, 0]
x_values = [-2.2, -1.2, -0.2, 0.8, 1.8]
y_values = [-0.27067, -0.3678, 0, 2.7183, 14.778]


def f_scipy(some_x, x_list, y_list):
    tck = interpolate.splrep(x_list, y_list)
    return interpolate.splev(some_x, tck)


def s_x(some_x, x_list, y_list, q_list, index):
    return q_list[index - 1] * (x_list[index] - some_x) ** 3 / 6 + \
           q_list[index] * (some_x - x_list[index - 1]) ** 3 / 6 + \
           ((y_list[index - 1] / 1) - q_list[index - 1] / 6) * (x_list[index] - some_x) + \
           ((y_list[index] / 1) - q_list[index] / 6) * (some_x - x_list[index - 1])


S_x_2 = s_x(x, x_values, y_values, q, 2)
S_x_3 = s_x(x, x_values, y_values, q, 3)

print("My implementation:", (S_x_2 + S_x_3) / 2)
print("Scipy implementation", f_scipy(x, x_values, y_values))
