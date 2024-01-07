import cmath
from copy import deepcopy
from math import sqrt
import sympy


def row_col_mul(row, col):
    return sum(map(lambda x, y: x * y, row, col))


def col_row_mul(col, row):
    return [[col[i] * row[j] for j in range(len(col))] for i in range(len(col))]


def matrix_matrix_mul(matrix1, matrix2):
    return [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0]))) for j in range(len(matrix2))] for i in
            range(len(matrix1[0]))]


def get_e_matrix(size):
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]


def sign(element):
    if element > 0:
        return 1
    elif element < 0:
        return -1
    return 0


def vector_second_norm_2(vector):
    return sqrt(sum([i * i for i in vector]))


def get_h(vector):
    upper = col_row_mul(vector, vector)
    lower = row_col_mul(vector, vector)
    E = get_e_matrix(len(upper))
    second = [[-2 / lower * i for i in j] for j in upper]
    return [[E[i][j] + second[i][j] for j in range(len(upper))] for i in range(len(upper))]


def gen_qr(matrix):
    A = deepcopy(matrix)
    H = []
    H_all = []
    vector = []
    for i in range(len(matrix) - 1):
        vector.clear()
        row = [A[j][i] for j in range(len(matrix))]
        vector += [0] * i
        vector.append(A[i][i] + sign(A[i][i]) * vector_second_norm_2(row[i:]))
        vector += row[i + 1:]
        H = get_h(vector)
        A = matrix_matrix_mul(H, A)
        H_all.append(H)
    Q = matrix_matrix_mul(H_all[0], H)
    R = A
    return Q, R


def solve_equation(equation: str, element: str):
    x = sympy.symbols(element)
    equ = sympy.Eq(eval(equation), 0)
    return sympy.solve(equ, x)


def gen_equ(l1, l2, l12):
    return f"({l1} - x)*({l2} - x) - {l12}"


def checker(matrix, epsilon):
    return sqrt(sum(matrix[i][0] ** 2 for i in range(1, len(matrix)))) > epsilon


def qr_solve(matrix, eps):
    A = deepcopy(matrix)
    while checker(A, eps):
        Q, R = gen_qr(A)
        A = matrix_matrix_mul(R, Q)
    return A[0][0], solve_equation(gen_equ(A[1][1], A[2][2], A[1][2] * A[2][1]), 'x')


if __name__ == '__main__':
    l1, expon = qr_solve([[1, 3, 1], [1, 1, 4], [4, 3, 1]], 0.01)
    print("Были найдены следующие собственные значения:\nL1 = {} \t L2 = {}\t L3 = {}\n".format(l1, *expon))
