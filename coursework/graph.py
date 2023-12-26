import numpy as np
import matplotlib.pyplot as plt
from Constants import G1, R


# Определение уравнений
def equation1(x, y, lst_g):
    arg1 = (2 * x - lst_g[0]) / (R*1100)
    arg2 = (x - lst_g[1]) / (R*1100)
    arg3 = (x + y - lst_g[2]) / (R*1100)
    arg4 = (2 * x + y - lst_g[3]) / (R*1100)
    res = 1/(R*1100) * (2 * np.exp(arg1) + np.exp(arg2) + np.exp(arg3) + 2 * np.exp(arg4)) - 1
    return res


def equation2(x, y, lst_g):
    arg1 = (2 * y - lst_g[0]) / (R*1100)
    arg2 = (y - lst_g[1]) / (R*1100)
    arg3 = (x + y - lst_g[2]) / (R*1100)
    arg4 = (2 * x + y - lst_g[3]) / (R*1100)
    res = 1/(R*1100) * (2 * np.exp(arg1) + np.exp(arg2) + np.exp(arg3) + np.exp(arg4)) - 1
    return res


# Создание сетки значений x1 и x2
x1 = np.linspace(-1, 1, 400)
x2 = np.linspace(-1, 1, 400)

# Создание сетки для уравнений
X1, X2 = np.meshgrid(x1, x2)
F1 = equation1(X1, X2, [G1["H2"]["1100"], G1["H"]["1100"], G1["OH"]["1100"], G1["H2O"]["1100"]])
F2 = equation2(X1, X2, [G1["O2"]["1100"], G1["O"]["1100"], G1["OH"]["1100"], G1["H2O"]["1100"]])

# Создание контурного графика для f1 и f2
plt.figure(figsize=(8, 6))
plt.contour(X1, X2, F1, levels=0, cmap='viridis')
plt.contour(X1, X2, F2, levels=0, cmap='viridis')

plt.colorbar(label='\nЗначения F1 и F2')
plt.xlabel('\nX1')
plt.ylabel('X2\n')
plt.title('Контурный график F1 и F2\n')
plt.show()