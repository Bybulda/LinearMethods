from UsefullFunc.UsefullPackage import read_matrix_from_file


def find_index(matrix, x):
    for i in range(len(matrix[0]) - 1):
        if matrix[0][i] <= x <= matrix[0][i + 1]:
            return i
    return 0


def find_side(i, f, x):
    return (f[i] - f[i - 1]) / (x[i] - x[i - 1])


def find_diffs(matrix, x):
    i = find_index(matrix, x)
    xs, f = matrix
    left_side = find_side(i + 1, f, xs)
    right_side = find_side(i + 2, f, xs)
    first_deriv = left_side + (2 * x - (xs[i] + xs[i + 1])) * ((left_side - right_side) / (xs[i] - xs[i + 2]))
    second_deriv = 2 * (left_side - right_side) / (xs[i] - xs[i + 2])
    return first_deriv, second_deriv


if __name__ == '__main__':
    matr, x = read_matrix_from_file('input.txt')
    first, second = find_diffs(matr, x[0])
    print(f"Первая производная равна: {first}\n"
          f"Вторая производная равна: {second}")
