import numpy as np
import matplotlib.pyplot as plt
from coursework.constants_equations.Constants import G1
import json


def plot_graph(conc, val):
    colors = ['b', 'r', 'g', 'y', 'purple', 'black']
    temp_values = [int(i) for i in range(1100, 6000, 100)]
    fig = plt.figure(figsize=(15, 8))
    gs = fig.add_gridspec(3, )
    axis = gs.subplots()
    for j in range(3):
                # plt.xlabel("Temperature")
                # plt.ylabel(f"Concentration = {val[j]}")
                for pos, key in enumerate(conc[0].keys()):
                    axis[j].plot(temp_values, conc[j][key], color=colors[pos], label=key)
                    axis[j].set(xlabel="Temperature", ylabel=f'Concentration O = {val[j]}')
                axis[j].legend()
    plt.show()


def get_points(concentration):
    result = {"H2O": [], "H2": [], "O2": [], "H": [], "O": [], "OH": [], }
    for i in range(1100, 6000, 100):
        with open(f"../data_{concentration}/{i}.json", 'r') as file:
            data = json.load(file)
            for key in result.keys():
                result[key].append(data[key])
    print(result)
    return result

concentration_02 = get_points(0.2)
concentration_033 = get_points(0.33)
concentration_05 = get_points(0.5)
plot_graph([concentration_05, concentration_02, concentration_033], [0.5, 0.2, 0.33])
