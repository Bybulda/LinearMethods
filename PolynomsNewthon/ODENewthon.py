from math import pi, sin
from functools import reduce
from sympy import simplify


def function(x: float) -> float:
    return sin(x) + x


# рекурсивная функция вычетов, из высших - нижние, разность сверху вычетов функций низших порядков
def get_subtraction(points: [float], func_x: [float], i: int, power: int) -> float:
    if power == 1:
        return (func_x[i + 1] - func_x[i]) / (points[i + 1] - points[i])
    return (get_subtraction(points, func_x, i + 1, power - 1) - get_subtraction(points, func_x, i, power - 1)) / (
            points[i + power] - points[i])


def get_lagr_str(func: callable, points: [float]):
    str_view_mns = [f"(x - {x})" for x in points]
    res = []
    for i in range(len(points)):
        curr = f"{''.join(str_view_mns[:i + 1])} / {''.join(f'({points[i]} - {points[j]})' for j in range(len(points)) if i != j)} * {func(points[i])}"
        res.append(curr)
    return ' + '.join(res)


def gen_lagranzh_polynom(func: callable, points: [float], x_: float) -> ([float], float):
    result = []
    str_view = get_lagr_str(func, points)
    for i in range(len(points)):
        f_i = func(points[i])
        upper_half = reduce(lambda x, y: x * y, [x_ - points[j] for j in range(len(points)) if i != j])
        lower_half = reduce(lambda x, y: x * y, [points[i] - points[j] for j in range(len(points)) if i != j])
        result.append(f_i * (upper_half / lower_half))
    return sum(result), abs(func(x_) - sum(result)), str_view


def gen_newthon_polynom(func: callable, points: [float], x_: float) -> ([float], float):
    fnc_x = [func(i) for i in points]
    result = [fnc_x[0]]
    str_view_mns = [f"(x - {x})" for x in points]
    str_view_polynom = [f"{fnc_x[0]}"]
    prod = n = 1
    for i in range(len(points) - 1):
        prod *= (x_ - points[i])
        current_subtraction_f = get_subtraction(points, fnc_x, 0, n)
        result.append(prod * current_subtraction_f)
        str_view_polynom.append(f'{current_subtraction_f}{"".join(str_view_mns[:i + 1])}')
        n += 1
    return sum(result), abs(func(x_) - sum(result)), ' + '.join(str_view_polynom)


if __name__ == '__main__':
    x1 = [i * pi / 6 for i in range(4)]
    x2 = [0, pi / 6, pi / 4, pi / 2]
    print(f'Набор точек X1: {x1}\nНабор точек X2: {x2}')

    print('Значение полинома Ньютона для набора точек X1: {0}\nПогрешность метода: {1}\nПостроенный полином: {2}'.format(
        *gen_newthon_polynom(function, x1, 1)))
    print('Значение полинома Ньютона для набора точек X1: {}\nПогрешность метода: {}\nПостроенный полином: {}'.format(
        *gen_newthon_polynom(function, x2, 1)))

    print(
        'Значение полинома Лагранжа для набора точек X1: {}\nПогрешность метода: {}\nПостроенный полином: {}'.format(
            *gen_lagranzh_polynom(function, x1, 1)))
    print(
        'Значение полинома Лагранжа для набора точек X1: {}\nПогрешность метода: {}\nПостроенный полином: {}'.format(
            *gen_lagranzh_polynom(function, x2, 1)))
