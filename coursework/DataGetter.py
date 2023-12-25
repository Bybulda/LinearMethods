import json


def count_g0(delta_h, h0_minus_h, t, f):
    return 1000 * delta_h - 1000 * h0_minus_h - t * f


def load_data(filename, key, table):
    with open(filename, 'r') as file:
        *list_numbers, h0, delta = [float(i.strip()) for i in file.readlines()]
        for value in range(len(list_numbers)):
            temperature = 1100 + value * 100
            table[key][temperature] = count_g0(delta, h0, temperature, list_numbers[value])


def fill_table(key_argv, filename_argv):
    G = {key: {} for key in key_argv}
    for i in range(len(key_argv)):
        load_data(filename_argv[i], key_argv[i], G)
    print(json.dumps(G, indent=4))


if __name__ == '__main__':
    fill_table(["H2O", "H2", "H", "OH", "O2", "O"], ["h2o", "h2", "h", "oh", "o2", "o"])
