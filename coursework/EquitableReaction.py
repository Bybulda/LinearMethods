from Constants import *
from Calculations import *
from system_ode.systemode import newton_method


def process_reaction(temperature, concentration_o0, concentration_h0):
    current_g = {key: G[key][f"{temperature}"] for key in G.keys()}
    print(current_g)


if __name__ == '__main__':
    print("Пожалуйста, введите концентрацию O: ")
    concentration_o0 = float(input())
    print("Пожалуйста, введите концентрацию H: ")
    concentration_h0 = float(input())
    print(
        "Пожалуйста, введите значение температуры в диапазоне 1000 < T < 6000, вводимо число должно быть кратно 100: ")
    temperature = int(input())
    process_reaction(temperature, concentration_o0, concentration_h0)
