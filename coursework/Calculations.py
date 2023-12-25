from Constants import *
from math import log, exp


def find_g0(t: int, element: str):
    return G[element.upper()][t]


def concentration_h(zh, gh, T):
    return P0 / (p * R * T) * exp((zh - gh) / (R * T))


def concentration_o(zo, go, T):
    return P0 / (p * R * T) * exp((zo - go) / (R * T))


def concentration_h2(zh, gh2, T):
    return P0 / (p * R * T) * exp((2 * zh - gh2) / (R * T))


def concentration_o2(zo, go2, T):
    return P0 / (p * R * T) * exp((2 * zo - go2) / (R * T))


def concentration_oh(zh, zo, goh, T):
    return P0 / (p * R * T) * exp((zh + zo - goh) / (R * T))


def concentration_h20(zh, zo, gh20, T):
    return P0 / (p * R * T) * exp((2 * zh + zo - gh20) / (R * T))


def f1_dzh(zh, zo, gh, gh2, goh, gh2o, T):
    return P0 / (p * R * T * R * T) * (
            exp((zh - gh) / (R * T)) + 4 * exp((2 * zh - gh2) / (R * T)) + exp((zh + zo - goh) / (R * T)) + 2 * exp(
        (2 * zh + zo - gh2o) / (R * T)))


def f1_dzo(zh, zo, goh, gh2o, T):
    return P0 / (p * R * T * R * T) * (exp((zo + zh - goh) / (R * T)) + exp((zo + 2 * zh - gh2o) / (R * T)))


def f2_dzh(zh, zo, goh, gh2o, T):
    return P0 / (p * R * T * R * T) * (exp((zo + zh - goh) / (R * T)) + 2 * exp((zo + 2 * zh - gh2o) / (R * T)))


def f2_dzo(zh, zo, go, go2, goh, gh2o, T):
    return P0 / (p * R * T * R * T) * (
            exp((zo - go) / (R * T)) + 4 * exp((2 * zo - go2) / (R * T)) + exp((zo + zh - goh) / (R * T)) + exp(
        (2 * zh + zo - gh2o) / (R * T)))
