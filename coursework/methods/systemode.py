from additional_methods import *

# Выводим результаты с точностью 4 знака после запятой
np.set_printoptions(precision=5, suppress=True)


# Метод простой итерации для решения системы нелинейных уравнений
def simple_iteration_method(phi1, phi2, x0, max_iterations, epsilon=1e-3):
    x = np.array(x0, dtype=float)
    i = 0

    for i in range(max_iterations):
        x1 = phi1(x[0], x[1])
        x2 = phi2(x[0], x[1])
        x_next = np.array([x1, x2])

        if np.linalg.norm(x_next - x) < epsilon:
            return x_next, i

        x = x_next

    print("Метод Простой итерации не сошелся за заданное количество итераций!")
    return x_next, i


# Метод Ньютона для решения системы нелинейных уравнений
def newton_method(f1, f2, df1_dx1, df1_dx2, df2_dx1, df2_dx2, x0, max_iterations, temperature, concentration_h,
                  concentration_o, epsilon=1e-3):
    x = np.array(x0, dtype=float)
    i = 0

    for i in range(max_iterations):
        f = np.array([f1(x[0], x[1], temperature, concentration_h), f2(x[0], x[1], temperature, concentration_o)])
        jacobian = np.array([[df1_dx1(x[0], x[1], temperature), df1_dx2(x[0], x[1], temperature)],
                             [df2_dx1(x[0], x[1], temperature), df2_dx2(x[0], x[1], temperature)]])

        try:

            delta_x = solve_linear_system(jacobian, -f)
            x_next = x + delta_x
        except np.linalg.LinAlgError:
            print("Сингулярная матрица Якоби. Метод Ньютона не сработал")
            break

        if np.linalg.norm(delta_x) < epsilon:
            return x_next, i

        x = x_next

    print("Метод Ньютона не сошелся за заданное количество итераций!")
    return x_next, i
