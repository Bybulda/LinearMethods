from Constants import *
# from math import log, exp
from numpy import exp


def func1(zh, zo, t, conc):
    return 2 * concentration_h2(zh, t) + concentration_h(zh, t) + concentration_oh(zh, zo, t) + \
        2 * concentration_h20(zh, zo, t) - conc


def func2(zh, zo, t, conc):
    return 2 * concentration_o2(zo, t) + concentration_o(zo, t) + concentration_oh(zh, zo, t) + \
        concentration_h20(zh, zo, t) - conc


def concentration_h(zh, T):
    gh = G1["H"][f"{T}"]
    return P0 / (p * R * T) * exp(zh - gh / (R * T))


def concentration_o(zo, T):
    go = G1["O"][f"{T}"]
    return P0 / (p * R * T) * exp(zo - go / (R * T))


def concentration_h2(zh, T):
    gh2 = G1["H2"][f"{T}"]
    return P0 / (p * R * T) * exp(2 * zh - gh2 / (R * T))


def concentration_o2(zo, T):
    go2 = G1["O2"][f"{T}"]
    return P0 / (p * R * T) * exp(2 * zo - go2 / (R * T))


def concentration_oh(zh, zo, T):
    goh = G1["OH"][f"{T}"]
    return P0 / (p * R * T) * exp(zh + zo - goh / (R * T))


def concentration_h20(zh, zo, T):
    gh20 = G1["H2O"][f"{T}"]
    return P0 / (p * R * T) * exp(2 * zh + zo - gh20 / (R * T))


def f1_dzh(zh, zo, T):
    gh, gh2, goh, gh2o = G1["H"][f"{T}"], G1["H2"][f"{T}"], G1["OH"][f"{T}"], G1["H2O"][f"{T}"]
    h = exp(zh - gh / (R * T))
    h2 = 4 * exp(2 * zh - gh2 / (R * T))
    oh = exp(zh + zo - goh / (R * T))
    h2o = 4 * exp(2 * zh + zo - gh2o / (R * T))
    return P0 / (p * R * T) * (h2 + h + oh + h2o)


def f1_dzo(zh, zo, T):
    goh, gh2o = G1["OH"][f"{T}"], G1["H2O"][f"{T}"]
    oh = exp(zo + zh - goh / (R * T))
    h2o = 2 * exp(zo + 2 * zh - gh2o / (R * T))
    return P0 / (p * R * T) * (oh + h2o)


def f2_dzh(zh, zo, T):
    goh, gh2o = G1["OH"][f"{T}"], G1["H2O"][f"{T}"]
    oh = exp(zo + zh - goh / (R * T))
    h2o = 2 * exp(zo + 2 * zh - gh2o / (R * T))
    return P0 / (p * R * T) * (oh + h2o)


def f2_dzo(zh, zo, T):
    go, go2, goh, gh2o = G1["O"][f"{T}"], G1["O2"][f"{T}"], G1["OH"][f"{T}"], G1["H2O"][f"{T}"]
    o = exp(zo - go / (R * T))
    o2 = 4 * exp(2 * zo - go2 / (R * T))
    oh = exp(zo + zh - goh / (R * T))
    h2o = exp(2 * zh + zo - gh2o / (R * T))
    return P0 / (p * R * T) * (o2 + o + oh + h2o)
