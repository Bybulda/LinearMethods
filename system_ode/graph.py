import numpy as np
import matplotlib.pyplot as plt

# Определение уравнений
def equation1(x1, x2, a):
    return x1 - np.cos(x2) - a

def equation2(x1, x2, a):
    return x2 - np.sin(x1) - a

# Значение параметра a
a = 3

# Создание сетки значений x1 и x2
x1 = np.linspace(-10, 10, 400)
x2 = np.linspace(-10, 10, 400)

# Создание сетки для уравнений
X1, X2 = np.meshgrid(x1, x2)
F1 = equation1(X1, X2, a)
F2 = equation2(X1, X2, a)

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
