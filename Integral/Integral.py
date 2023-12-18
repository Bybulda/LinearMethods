def y(x):
    return x / (x ** 3 + 8)


def trapezoidal_rule(func, a, b, h):
    n = int((b - a) / h)
    result = 0.5 * (func(a) + func(b))

    for i in range(1, n):
        result += func(a + i * h)

    result *= h
    return result


def simpson_rule(func, a, b, h):
    n = int((b - a) / h)
    result = func(a) + func(b)

    for i in range(1, n, 2):
        result += 4 * func(a + i * h)

    for i in range(2, n - 1, 2):
        result += 2 * func(a + i * h)

    result *= h / 3
    return result


def rectangle_rule(func, a, b, h, side='right'):
    n = int((b - a) / h)
    rng = (1, n + 1) if side == 'right' else (0, n)
    result = 0

    for i in range(*rng):
        result += func(a + i * h)

    result *= h
    return result


def runge_romberg_error(func, method, h1, h2, x0, xk, p, optional=None):
    res1 = method(func, x0, xk, h1, optional) if optional is not None else method(func, x0, xk, h1)
    res2 = method(func, x0, xk, h2, optional) if optional is not None else method(func, x0, xk, h2)
    error = abs(res2 - res1) / (2 ** p - 1)
    return error


if __name__ == '__main__':
    x0, xk = -1, 1
    h1, h2 = 0.001, 0.0005
    print(
        f'Результаты вычисления определенного интеграла функции y = x / (x^3 + 8) на отрезке [-1, 1] с h1 = 0.5 и h2 = 0.25')
    print(f'Решение методом Симпсона: \nh1: {simpson_rule(y, x0, xk, h1)}\th2: {simpson_rule(y, x0, xk, h2)}')
    print(f'Оценка погрешности методом Рунге-Ромберга: {runge_romberg_error(y, simpson_rule, h1, h2, x0, xk, 3)}\n')
    print(f'Решение методом Трапеций: \nh1: {trapezoidal_rule(y, x0, xk, h1)}\th2: {trapezoidal_rule(y, x0, xk, h2)}')
    print(f'Оценка погрешности методом Рунге-Ромберга: {runge_romberg_error(y, trapezoidal_rule, h1, h2, x0, xk, 1)}\n')
    print(
        f'Решение методом Левых Прямоугольников: \nh1: {rectangle_rule(y, x0, xk, h1, "left")}\th2: {rectangle_rule(y, x0, xk, h1, "left")}')
    print(
        f'Оценка погрешности методом Рунге-Ромберга: {runge_romberg_error(y, rectangle_rule, h1, h2, x0, xk, 1, "left")}\n')
    print(
        f'Решение методом Левых Прямоугольников: \nh1: {rectangle_rule(y, x0, xk, h1)}\th2: {rectangle_rule(y, x0, xk, h1)}')
    print(
        f'Оценка погрешности методом Рунге-Ромберга: {runge_romberg_error(y, rectangle_rule, h1, h2, x0, xk, 1)}\n')
