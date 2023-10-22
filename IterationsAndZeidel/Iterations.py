from copy import deepcopy
from UsefullFunc.UsefullPackage import read_matrix_from_file


def dot_product(a, b):
    """Calculate the dot product of two lists."""
    return sum(x * y for x, y in zip(a, b))


def subtract_vectors(a, b):
    """Subtract one list from another element-wise."""
    return [x - y for x, y in zip(a, b)]


def norm(vector):
    """Calculate the Euclidean norm (2-norm) of a list."""
    return max(vector)


def normal_view(matrix, vector) -> [[[float]], [float]]:
    res = deepcopy(matrix)
    res_v = vector[:]
    for i in range(len(res)):
        delim = res[i][i]
        for j in range(len(res)):
            res[i][j] /= -delim
        res_v[i] /= delim
        res[i][i] = 0
    return res, res_v


def sum_vectors(vect1, vect2):
    return list(map(lambda x, y: x + y, vect1, vect2))


def prod_matrix(a, vector):
    return [sum(map(lambda x, y: x * y, a[i], vector)) for i in range(len(a))]


def gauss_seidel(a, b, epsilon):
    a_norm, b_norm = normal_view(a, b)
    alpha_norm = max(max(i) for i in a_norm)
    x_start = [0] * len(a_norm)
    x_new = b_norm[:]

    while True:
        if norm(subtract_vectors(x_new, x_start)) <= epsilon:
            break
        x_start = x_new[:]
        for j in range(len(a_norm)):
            x_res = 0
            for l in range(len(a_norm)):
                x_res += x_new[l] * a_norm[j][l]
            x_res += b_norm[j]
            x_new[j] = x_res
    return x_new


def simple_iteration(a, b, epsilon):
    a_norm, b_norm = normal_view(a, b)
    alpha_norm = max(max(i) for i in a_norm)
    x_start = [0] * len(a_norm)
    max_iters = 100000
    x_new = b_norm[:]

    for j in range(max_iters):
        if norm(subtract_vectors(x_new, x_start)) > epsilon:
            x_start = x_new[:]
            x_new = sum_vectors(prod_matrix(a_norm, x_new), b_norm)
        else:
            break
    return x_new


if __name__ == '__main__':
    a, b = read_matrix_from_file('matrix.txt')

    solution = simple_iteration(a, b, 1e-6)
    sol = gauss_seidel(a, b, 1e-6)
    print("Solution iters:", [round(i, 6) for i in solution])
    print("Solution Zeidel", [round(i, 6) for i in sol])
