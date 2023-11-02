import sys
from copy import deepcopy
from math import sin, cos, atan, pi

from UsefullFunc.UsefullPackage import multiply_matrix, find_transport_matrix, \
    multiply_matrix_vector, read_matrix_from_file, scholar_multiply


def divide_vector(vector: [float], divider: float) -> [float]:
    return [i / divider for i in vector]


def find_norm_vector(vector: [float]) -> float:
    return max(vector)


def find_max_non_diagonal(matrix: [[float]]) -> [float, int, int]:
    max_el = [matrix[0][1], 0, 1]
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if abs(max_el[0]) < abs(matrix[i][j]):
                max_el = [matrix[i][j], i, j]
    return max_el


def find_phi(matrix: [[float]], i: int, j: int) -> float:
    if matrix[i][i] == matrix[j][j]:
        return pi / 4
    phi = 0.5 * (atan((2 * matrix[i][j]) / (matrix[i][i] - matrix[j][j])))
    return 0.5 * (atan((2 * matrix[i][j]) / (matrix[i][i] - matrix[j][j])))


def make_rotation_matrix(angle: float, size: int, i_: int, j_: int) -> [[float]]:
    res = [[1. if i == j else 0. for j in range(size)] for i in range(size)]
    res[i_][j_], res[j_][i_], res[i_][i_], res[j_][j_] = round(-sin(angle), 6), round(sin(angle), 6), \
        round(cos(angle), 6), round(cos(angle), 6)
    return res


def find_lim(matrix: [[float]]) -> float:
    res = 0
    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            res += matrix[i][j] * matrix[i][j]
    return res ** 0.5


def powers_solution(matrix: [[float]], epsilon: float) -> [[float], float]:
    matrix_y = matrix
    lambdas, my_vectors = None, None
    j = 0
    last_two = []
    y_prev = [1] * len(matrix)
    while True:
        if len(last_two) == 2:
            if abs(last_two[1] - last_two[0]) < epsilon:
                lambdas = last_two[1]
                my_vectors = y_prev
                j += 1
                break
            z_k = multiply_matrix_vector(matrix_y, y_prev)
            #  подписать что это
            last_two[0], last_two[1] = last_two[1], z_k[j] / y_prev[j]
            y_prev = divide_vector(z_k, find_norm_vector(z_k))
        else:
            z_k = multiply_matrix_vector(matrix_y, y_prev)
            last_two.append(z_k[j] / y_prev[j])
            y_prev = divide_vector(z_k, find_norm_vector(z_k))
    return my_vectors, lambdas


def rotation_solution(matrix: [[float]], epsilon: float) -> [[[float]], [float]]:
    matrix_a = deepcopy(matrix)
    #   first step
    matrix_res_u = [[1 if i == j else 0 for i in range(len(matrix))] for j in range(len(matrix))]
    while abs(find_lim(matrix_a)) > epsilon:
        # надо найти макс по модулю наддиагональный элемент
        res_ij = find_max_non_diagonal(matrix_a)
        # матрица вращения по формуле
        matrix_u = make_rotation_matrix(find_phi(matrix_a, *res_ij[1:]), len(matrix_a), *res_ij[1:])
        # собираем матрицу результат св
        matrix_res_u = multiply_matrix(matrix_res_u, matrix_u)
        # A^k+1 = U^t*A^k^U
        matrix_a = multiply_matrix(multiply_matrix(find_transport_matrix(matrix_u), matrix_a), matrix_u)
    result_vector = [[matrix_res_u[j][i] for j in range(len(matrix_res_u)) for i in range(len(matrix_res_u))]]
    if scholar_multiply(matrix_res_u[0], matrix_res_u[1]) > epsilon or scholar_multiply(matrix_res_u[0], matrix_res_u[
        2]) > epsilon or scholar_multiply(matrix_res_u[1], matrix_res_u[2]) > epsilon:
        raise Exception("Something went wrong for this matrix!")
    return matrix_res_u, [matrix_a[i][i] for i in range(len(matrix_a))]


if __name__ == '__main__':
    matrix, epsilon = read_matrix_from_file(sys.argv[1])
    vector, num = powers_solution(matrix, epsilon[0])
    print("Solution for Rotation method: ", *rotation_solution(matrix, epsilon[0]))
    print("Solution for Powers method spectral radius: ", [i * 0.81 for i in vector], num, sep=" ")
