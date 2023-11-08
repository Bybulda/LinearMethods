import math
from functools import reduce


def function(x: float) -> float:
    return math.sin(x) + x


# рекурсивная функция вычетов, из высших - нижние, разность сверху вычетов функций низших порядков
def get_subtraction(points: [float], func_x: [float], i: int, power: int) -> float:
    if power == 1:
        return (func_x[i + 1] - func_x[i]) / (points[i + 1] - points[i])
    return (get_subtraction(points, func_x, i + 1, power - 1) - get_subtraction(points, func_x, i, power - 1)) / (
            points[i + power] - points[i])


# найти полином и погрешность в точке
def gen_newthon_polynom(func: callable, points: [float], x_: float) -> ([float], float):
    result = []
    for i in range(len(points)):
        f_i = func(points[i])
        upper_half = reduce(lambda x, y: x * y, [x_ - points[j] for j in range(len(points)) if i != j])
        lower_half = reduce(lambda x, y: x * y, [points[i] - points[j] for j in range(len(points)) if i != j])
        result.append(f_i * (upper_half / lower_half))
    return result, abs(func(x_) - sum(result))


def gen_lagranzh_polynom(func: callable, points: [float], x_: float) -> ([float], float):
    fnc_x = [func(i) for i in points]
    result = [fnc_x[0]]
    prod = n = 1
    for i in range(len(points) - 1):
        prod *= (x_ - points[i])
        current_subtraction_f = get_subtraction(points, fnc_x, 0, n)
        result.append(prod * current_subtraction_f)
        n += 1
    return result, abs(func(x_) - sum(result))


print(gen_newthon_polynom(function, [i / 6 * math.pi for i in range(4)], 1))
print(gen_lagranzh_polynom(function, [i / 6 * math.pi for i in range(4)], 1))
