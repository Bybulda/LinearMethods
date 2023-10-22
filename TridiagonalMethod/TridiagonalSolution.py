import sys
from functools import reduce


class NotANeededMatrix(Exception):
    def __str__(self):
        return "Sorry this matrix doesnt fit the requirements!\n"


def find_det(matrix: [[float]]) -> float:
    det = 1
    for i in range(len(matrix)):
        det *= matrix[i][i]
    return det


def check_coefficients(a=None, b=None, c=None):
    if a == 0 or b == 0:
        raise NotANeededMatrix
    elif c is not None and a is None and not (abs(b) >= abs(c)):
        raise NotANeededMatrix
    elif a is not None and c is None and not (abs(b) >= abs(a)):
        raise NotANeededMatrix
    elif a is not None and c is not None and not (abs(b) >= abs(a) + abs(c)):
        raise NotANeededMatrix


def tridiagonal_solution(matrix: [[float]], vector_b: [float]) -> [float]:
    check_coefficients(b=matrix[0][0], c=matrix[0][1])
    vector_alphas = [-matrix[0][1] / matrix[0][0]]
    vector_betas = [vector_b[0] / matrix[0][0]]

    for i in range(1, len(matrix) - 1):
        check_coefficients(matrix[i][i - 1], matrix[i][i], matrix[i][i + 1])
        y_i = matrix[i][i] + matrix[i][i - 1] * vector_alphas[i - 1]
        a_i = -matrix[i][i + 1] / y_i
        b_i = (vector_b[i] - matrix[i][i - 1] * vector_betas[i - 1]) / y_i
        vector_alphas.append(a_i)
        vector_betas.append(b_i)

    check_coefficients(a=matrix[-1][-2], b=matrix[-1][-1])
    y_n = (matrix[-1][-1] + matrix[-1][-2] * vector_alphas[-1])
    vector_x = [round((vector_b[-1] - matrix[-1][-2] * vector_betas[-1]) / y_n, 6)]

    for i in range(len(matrix) - 2, -1, -1):
        vector_x.insert(0, round(vector_alphas[i] * vector_x[0] + vector_betas[i], 6))

    return vector_x


def read_from_file(file: str) -> None:
    with open(file, 'r') as file:
        *matrix_a, vector_f = [[float(j) for j in i.split()] for i in file.read().split('\n') if len(i) != 0]
    find_det(matrix_a)
    solution = tridiagonal_solution(matrix_a, vector_f)
    print("The solution for matrix:\n", '\n'.join('\t'.join(str(i) for i in j) for j in matrix_a),
          "\nIs this vector:\n", " ".join(str(i) for i in solution))
    # print("\ndeterminant = ", find_det(matrix_a))


if __name__ == '__main__':
    try:
        read_from_file(sys.argv[1])
    except NotANeededMatrix:
        print("Try another one!")
