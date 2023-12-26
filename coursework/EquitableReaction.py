from Constants import *
from Calculations import *
from systemode import newton_method


def process_reaction(temperature, concentration_o0, concentration_h0):
    start_zh_zo = [-0.319, 0.424]
    zh_zo, iters = newton_method(func1, func2, f1_dzh, f1_dzo, f2_dzh, f2_dzo, start_zh_zo, 100, temperature,
                                 concentration_o0, concentration_h0)
    zh, zo = zh_zo
    h, h2, o, o2 = concentration_h(zh, temperature), concentration_h2(zh, temperature), \
        concentration_o(zo, temperature), concentration_o2(zo, temperature)
    oh, h2o = concentration_oh(zh, zo, temperature), concentration_h20(zh, zo, temperature)
    print(h, h2, o, o2, oh, h2o)
    print(2*h2 + h + oh + 2*h2o)
    print(2 * o2 + o + oh + h2o)


if __name__ == '__main__':
    print("Пожалуйста, введите концентрацию O: ")
    concentration_o0 = float(input())
    print("Пожалуйста, введите концентрацию H: ")
    concentration_h0 = float(input())
    print(
        "Пожалуйста, введите значение температуры в диапазоне 1000 < T < 6000, вводимо число должно быть кратно 100: ")
    temperature = int(input())
    process_reaction(temperature, concentration_o0, concentration_h0)
