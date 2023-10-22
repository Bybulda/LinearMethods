import sys
from copy import deepcopy


class MultipleSolutionsError(Exception):
    def __str__(self):
        return "Matrix has infinity number of solutions!"


class ZeroSolutionsError(ZeroDivisionError):
    def __str__(self):
        return "Matrix has no solutions!"


def swap_matrix_rows(matrix: [[float]], first_row: int, second_row: int) -> None:
    for i in range(len(matrix[0])):
        matrix[first_row][i], matrix[second_row][i] = matrix[second_row][i], matrix[first_row][i]


def swap_coefficients_row(coefficients: [float], first_row: int, second_row: int) -> None:
    coefficients[first_row], coefficients[second_row] = coefficients[second_row], coefficients[first_row]


def eliminate_matrix_rows(matrix: [[float]], to_eliminate: int, eliminate_by: int, coefficient: float) -> None:
    for i in range(len(matrix)):
        matrix[to_eliminate][i] = round(matrix[to_eliminate][i] + matrix[eliminate_by][i] * coefficient, 6)


def eliminate_vector_rows(coefficients: [float], to_eliminate: int, eliminate_by: int, coefficient: float) -> None:
    coefficients[to_eliminate] = round(coefficients[to_eliminate] + coefficients[eliminate_by] * coefficient, 6)


def swap_rows(matrix: [[float]], coefficients: [[float]], first_row: int, second_row: int, func: callable) -> None:
    swap_matrix_rows(matrix, first_row, second_row)
    func(coefficients, first_row, second_row)


def find_not_zero(matrix: [[float]], column: int) -> int:
    mx = matrix[column][0]
    pos = 0
    for i in range(column, len(matrix)):
        if matrix[i][column] > mx:
            mx = matrix[i][column]
            pos = i
    return pos


def divide_row(matrix: [[float]], coefficients: [[float]], row: int, coefficient: float) -> None:
    for i in range(len(matrix)):
        matrix[row][i] = round(matrix[row][i] * coefficient, 6)
        coefficients[row][i] = round(coefficients[row][i] * coefficient, 6)


def eliminate_row(matrix: [[float]], coefficients: [[float]] or [float], to_eliminate: int,
                  eliminate_by: int, coefficient: float, func: callable) -> None:
    eliminate_matrix_rows(matrix, to_eliminate, eliminate_by, coefficient)
    func(coefficients, to_eliminate, eliminate_by, coefficient)


def make_upper_triangular_matrix(matrix_a: [[float]], coefficients_row: [[float]] or [float]) -> float:
    rows, cols = len(matrix_a), len(matrix_a[0])
    counter = 0
    func_swap = swap_matrix_rows if isinstance(coefficients_row[0], list) else swap_coefficients_row
    func_eliminate = eliminate_matrix_rows if isinstance(coefficients_row[0], list) else eliminate_vector_rows
    for i in range(rows - 1):
        great_element = find_not_zero(matrix_a, i)
        if great_element != 0:
            swap_rows(matrix_a, coefficients_row, great_element, i, func_swap)
            counter += 1
        for j in range(i + 1, rows):
            if matrix_a[j][i] != 0 and matrix_a[i][i] != 0:
                eliminate_row(matrix_a, coefficients_row, j, i, -1 * (matrix_a[j][i] / matrix_a[i][i]), func_eliminate)
    det = 1
    for i in range(rows):
        det *= matrix_a[i][i]
    return ((-1) ** counter) * det


def gaussian_solve(matrix_a: [[float]], coefficients_row: [float]) -> [[float], float]:
    det = make_upper_triangular_matrix(matrix_a, coefficients_row)
    if det == 0:
        raise MultipleSolutionsError
    vector_x = []
    size = len(matrix_a)
    for i in range(size - 1, -1, -1):
        counter, summary = -1, 0
        for j in range(size - 1, i, -1):
            summary += matrix_a[i][j] * vector_x[counter]
            counter -= 1
        try:
            solved_x_n = (coefficients_row[i] - summary) / matrix_a[i][i]
        except ZeroDivisionError:
            raise ZeroSolutionsError
        vector_x.insert(0, round(solved_x_n, 6))
    return vector_x, det


def find_reversed_matrix(matrix: [[float]]) -> [[float], float]:
    size = len(matrix)
    matrix_e = [[1.0 if i == j else 0.0 for j in range(len(matrix))] for i in range(len(matrix))]
    det = make_upper_triangular_matrix(matrix, matrix_e)

    for i in range(size - 1, -1, -1):
        divide_row(matrix, matrix_e, i, 1 / matrix[i][i])
        for j in range(i - 1, -1, -1):
            eliminate_row(matrix, matrix_e, j, i, -1 * matrix[j][i], eliminate_matrix_rows)
    return matrix_e, det


def read_matrix_from_file(filename: str) -> None:
    with open(filename, "r") as file:
        *matrix, vector = [[float(j) for j in i.split()] for i in file.read().split('\n') if len(i) != 0]
    matrix_second = deepcopy(matrix)
    solution, det = gaussian_solve(matrix, vector)
    print("Solution for input matrix has these x's:\n", '\t'.join(f'{i}' for i in solution),
          "\nAnd determinant: ", det)
    print("\nThe reversed matrix:\n", '\n'.join('\t'.join(f'{i}' for i in j)
                                                for j in find_reversed_matrix(matrix_second)[0]))


if __name__ == '__main__':
    try:
        read_matrix_from_file(sys.argv[1])
    except ZeroSolutionsError:
        print("Try other matrix!")
    except MultipleSolutionsError:
        print("Cant find solution for this matrix!")
