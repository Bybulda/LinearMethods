from functools import reduce

from UsefullFunc.UsefullPackage import read_matrix_from_file
from GaussMethod.Gauss import gaussian_solve
import math
import numpy as np
import matplotlib.pyplot as plt


def get_sum_monom(x_j, power):
    return sum(math.pow(x_j[j], power) for j in range(len(x_j)))


def func_power1(x, a0, a1):
    return a0 + a1 * x


def func_power2(x, a0, a1, a2):
    return a0 + a1 * x + a2 * x ** 2


def quadratic_errors(func, x_i, f_i, coeffs):
    return sum(math.pow((func(x_i[i], *coeffs) * f_i[i]), 2) for i in range(len(x_i)))


def get_poly(x_i, f_i, power):
    n = power + 1
    matrix = [[0 for i in range(n)] for j in range(n)]
    vector = [0 for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j == 0:
                matrix[0][0] = len(x_i)
            else:
                matrix[i][j] = get_sum_monom(x_i, i + j)
        vector[i] = sum(map(lambda x, y: x * y, f_i, (math.pow(f, i) for f in x_i)))
    return matrix, vector


def mnk(x_i, f_i):
    res_power1 = gaussian_solve(*get_poly(x_i, f_i, 1))
    quadr_err1 = quadratic_errors(func_power1, x_i, f_i, res_power1[0])
    res_power2 = gaussian_solve(*get_poly(x_i, f_i, 2))
    quadr_err2 = quadratic_errors(func_power2, x_i, f_i, res_power2[0])
    print('Полученый многочлен первой степени имеет вид:\n F(x) = {} + {}*x\nСумма квадратов ошибок: {}'.format(
        *res_power1[0], quadr_err1))
    print('Полученый многочлен второй степени имеет вид:\n F(x) = {} + {}*x + {}x^2\nСумма квадратов ошибок: {}'.format(
        *res_power2[0], quadr_err2))
    plot_graph(x_i, f_i, res_power1[0], res_power2[0])


def plot_graph(x_i, f_i, coeffs1, coeffs2):
    x = np.linspace(x_i[0], x_i[-1], 100)
    y1 = [func_power1(y, *coeffs1) for y in x]
    y2 = [func_power2(y, *coeffs2) for y in x]
    y3 = np.linspace(f_i[0], f_i[-1], 100)
    plt.scatter(x_i, f_i, c='red', label='Function points')
    plt.plot(x, y1, label='Polynom first pow')
    plt.plot(x, y2, label='Polynom second pow')
    # plt.scatter(x, y3, label='Points', c='blue')
    plt.legend()
    plt.title('Cubic Spline Function')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


if __name__ == '__main__':
    x_i, f_i = read_matrix_from_file("input.txt")
    mnk(x_i[0], f_i)
