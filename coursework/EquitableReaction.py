import json

from Calculations import *
from systemode import newton_method


def json_write(filename: str, args: dict):
    with open(filename, 'w', encoding='utf-8') as file:
        result = {"H2O": args['h2o'], "H2": args['h2'], "O2": args['o2'], "H": args['h'], "O": args['o'],
                  "OH": args['oh'], "T": args['T'], "Concentration H": args["Ch"], "Concentration O": args["Co"]}
        json_dict = json.dumps(result, indent=4)
        file.write(json_dict)


def fancy_write(filename: str, args: dict):
    with open(filename, 'w', encoding='utf-8') as file:
        gamma_list = ['y'] * 10
        start_params = [args["Ch"], args["Co"], args["T"]]
        gamma_values_1 = [args["h2"], args["h"], args["oh"], args["h2o"], args["Ch"], args["s1"], args["Ch"]]
        gamma_values_2 = [args["o2"], args["o"], args["oh"], args["h2o"], args["Co"], args["s2"], args["Co"]]
        concentration_values = [args["h"], args["o"], args["h2"], args["o2"], args["oh"], args["h2o"]]
        file.write("При заданных концентрациях H: {} и O: {} и температуре: {} для решения системы уравнений:\n"
                   "2*{}H2 + {}H + {}OH + 2*{}H2O = {}H\n"
                   "2*{}O2 + {}O + {}OH + {}H2O = {}O\n\n"
                   "Были найдены следующие концентрации элементов:\n"
                   "H: {}\nO: {}\nH2: {}\nO2: {}\n"
                   "OH: {}\nH2O: {}\n\n"
                   "Итого система представляет собой:\n"
                   "2*{} + {} + {} + 2*{} = {} => {} = {}\n"
                   "2*{} + {} + {} + {} = {} => {} = {}\n".format(*start_params, *gamma_list, *concentration_values,
                                                                  *gamma_values_1, *gamma_values_2))


def process_reaction(temperature, concentration_o0, concentration_h0):
    start_zh_zo = [-0.319, 0.424]
    zh_zo, iters = newton_method(func1, func2, f1_dzh, f1_dzo, f2_dzh, f2_dzo, start_zh_zo, 100, temperature,
                                 concentration_h0, concentration_o0)
    zh, zo = zh_zo
    h, h2, o, o2 = concentration_h(zh, temperature), concentration_h2(zh, temperature), \
        concentration_o(zo, temperature), concentration_o2(zo, temperature)
    oh, h2o = concentration_oh(zh, zo, temperature), concentration_h20(zh, zo, temperature)
    answer = {"h2o": h2o, "oh": oh, "h": h, "o": o, "h2": h2, "o2": o2, "Ch": concentration_h0, "Co": concentration_o0,
              "T": temperature, 's1': 2 * h2 + h + oh + 2 * h2o, 's2': 2 * o2 + o + oh + h2o}
    fancy_write("result.txt", answer)
    json_write("result.json", answer)
    print(h, h2, o, o2, oh, h2o)
    print(2 * h2 + h + oh + 2 * h2o)
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
