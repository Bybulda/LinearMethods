from TridiagonalMethod.TridiagonalSolution import tridiagonal_solution as solution


def get_index(vector, x):
    for i in range(len(vector) - 1):
        if vector[i] <= x <= vector[i + 1]:
            return i
    return 0


def get_spline_matrix(x_i: [float], f_i: [float]) -> [[float]]:
    res = [[0 for i in range(len(x_i) - 2)] for j in range(len(x_i) - 2)]
    vector = [0] * (len(f_i) - 2)
    h_i = [x_i[i] - x_i[i - 1] for i in range(1, len(x_i))]
    res[0][0] = 2 * (h_i[0] + h_i[1])
    res[0][1] = h_i[1]
    vector[0] = 3 * ((f_i[2] - f_i[1]) / h_i[1] - (f_i[1] - f_i[0]) / h_i[0])
    j = 1
    for i in range(2, len(x_i) - 2):
        res[i - 1][i - 2] = h_i[i]
        res[i - 1][i - 1] = 2 * (h_i[i] + h_i[i + 1])
        res[i - 1][i] = h_i[i]
        vector[j] = 3 * ((f_i[i + 1] - f_i[i]) / h_i[i] - (f_i[i] - f_i[i - 1]) / h_i[i - 1])
        j += 1
    res[2][1] = h_i[2]
    res[2][2] = 2 * (h_i[2] + h_i[3])
    vector[2] = 3 * ((f_i[4] - f_i[3]) / h_i[3] - (f_i[3] - f_i[2]) / h_i[2])
    return res, vector


def get_spline(x_i, f_i, x):
    spline_matrix_and_vector = get_spline_matrix(x_i, f_i)
    h_i = [x_i[i] - x_i[i - 1] for i in range(1, len(x_i))]
    c_i = [0] + solution(*spline_matrix_and_vector)
    a_i = [f_i[i] for i in range(0, len(x_i) - 1)]
    d_i, b_i = [], []
    for i in range(1, len(x_i) - 1):
        b_i.append((f_i[i] - f_i[i - 1]) / h_i[i - 1] - 1 / 3 * (c_i[i] + 2 * c_i[i - 1]) * h_i[i - 1])
        d_i.append((c_i[i] - c_i[i - 1]) / (3 * h_i[i - 1]))
    b_i.append((f_i[4] - f_i[3]) / h_i[3] - 2 / 3 * h_i[3] * c_i[3])
    d_i.append(-c_i[3] / (3 * h_i[3]))
    index = get_index(x_i, x)
    res = a_i[index] + b_i[index] * (x - x_i[index]) + c_i[index] * (x - x_i[index]) ** 2 + d_i[
        index] * (x - x_i[index]) ** 3
    return res, a_i, b_i, c_i, d_i


print(get_spline([0.0, 0.9, 1.8, 2.7, 3.6], [0.0, 0.72235, 1.5609, 2.8459, 7.7275], 1.5))
