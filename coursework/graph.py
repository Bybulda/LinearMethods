import numpy as np
import matplotlib.pyplot as plt
from Constants import G1, R


# Определение уравнений
def equation1(x, y, lst_g):
    arg1 = (2 * x - lst_g[0]) / (R*1100)
    arg2 = (x - lst_g[1]) / (R*1100)
    arg3 = (x + y - lst_g[2]) / (R*1100)
    arg4 = (2 * x + y - lst_g[3]) / (R*1100)
    print(arg1, arg2, arg3, arg4)

    return 1/(R*1100) * (2 * np.exp(arg1) + np.exp(arg2) + np.exp(arg3) + 2 * np.exp(arg4)) - 0.001


def equation2(x, y, lst_g):
    arg1 = (2 * y - lst_g[0]) / (R*1100)
    arg2 = (y - lst_g[1]) / (R*1100)
    arg3 = (x + y - lst_g[2]) / (R*1100)
    arg4 = (2 * x + y - lst_g[3]) / (R*1100)
    print(arg1, arg2, arg3, arg4)
    return 1/(R*1100) * (2 * np.exp(arg1) + np.exp(arg2) + np.exp(arg3) + np.exp(arg4)) - 0.0001


# Значение параметра a
a = 3

# Создание сетки значений x1 и x2
x1 = np.linspace(-1, 1, 400)
x2 = np.linspace(-1, 1, 400)

# Создание сетки для уравнений
X1, X2 = np.meshgrid(x1, x2)
print(G1["H2"]["1100"], G1["H"]["1100"], G1["OH"]["1100"], G1["H2O"]["1100"])
print(G1["O2"]["1100"], G1["O"]["1100"], G1["OH"]["1100"], G1["H2O"]["1100"])
F1 = equation1(X1, X2, [G1["H2"]["1100"], G1["H"]["1100"], G1["OH"]["1100"], G1["H2O"]["1100"]])
F2 = equation2(X1, X2, [G1["O2"]["1100"], G1["O"]["1100"], G1["OH"]["1100"], G1["H2O"]["1100"]])

# Построение графика уравнения 1
plt.contour(X1, X2, F1, levels=[0], colors='r', label='x1 - cos(x2) - a = 0')

# Построение графика уравнения 2
plt.contour(X1, X2, F2, levels=[0], colors='b', label='x2 - sin(x1) - a = 0')

# Настройка графика
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('График уравнений')
plt.legend()
plt.grid(True)
plt.show()
