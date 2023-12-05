import math
import numpy as np


def function(x):
    return math.pow(3, x) - 5 * math.pow(x, 2) + 1
    # return math.pow(math.e, 2 * x) + 3 * x - 4


def function_der1(x):
    # return 2 * math.pow(math.e, 2 * x) + 3
    return math.pow(3, x) * math.log(3, math.e) - 10 * x


def func_der2(x):
    # return 4 * math.pow(math.e, 2 * x)
    return math.pow(3, x) * math.pow(math.log(3, math.e), 2) - 10


def phi_x(x):
    return math.sqrt((math.pow(3, x) + 1) / 5)
    # return (math.log(4 - 3 * x, math.e)) / 2


def phi_x_der(x):
    return (math.log(3, math.e) * math.pow(3, x)) / (2 * math.sqrt(5) * math.sqrt(math.pow(3, x) + 1))
    # return -3 / (2*(4 - 3 * x))


def find_q(interval):
    ranger = np.linspace(interval[0], interval[1], 1000)
    breaker = interval[0]
    for i in ranger:
        if abs(phi_x_der(i)) >= 1:
            break
        breaker = i
    return abs(phi_x_der(breaker))


def iteration_ode(interval, epsilon):
    print('k\t\tx^k\t\tphi(x^k)')
    x_pred = (interval[0] + interval[1]) / 2
    x_next = phi_x(x_pred)
    q = find_q(interval)
    counter = 0
    print(f"{counter}\t\t{x_pred}\t\t{x_next}")
    while (q / (1 - q)) * abs(x_next - x_pred) > epsilon:
        x_pred = x_next
        x_next = phi_x(x_pred)
        # q = find_q(x_pred)
        counter += 1
        print(f"{counter}\t\t{x_pred}\t\t{x_next}")
    return x_next, counter


def newthon_ode(interval, epsilon):
    if function(interval[1]) * func_der2(interval[1]) < 0:
        raise Exception
    print("k\t\tx^k\t\tf(x^k)\t\tf'(x^k)\t\t-f(x^k)/f'(x^k)")
    x_pred = interval[1]
    x_next = x_pred - (function(x_pred)) / (function_der1(x_pred))
    counter = 0
    print(
        f"{counter}\t\t{x_pred}\t\t{function(x_pred)}\t\t{function_der1(x_pred)}\t\t{-(function(x_pred)) / (function_der1(x_pred))}")
    while abs(x_next - x_pred) > epsilon:
        x_pred = x_next
        x_next = x_pred - (function(x_pred)) / (function_der1(x_pred))
        counter += 1
        print(
            f"{counter}\t\t{x_pred}\t\t{function(x_pred)}\t\t{function_der1(x_pred)}\t\t{-(function(x_pred)) / (function_der1(x_pred))}")
    return x_next, counter


def main():
    pass


if __name__ == '__main__':
    # interval = [0.4, 0.6]
    interval = [0.5, 1]
    print(newthon_ode(interval, 0.001))
    print(iteration_ode(interval, 0.001))
