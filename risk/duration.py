import numpy as np

def modified_duration(cashflows, ytm, times):
    pv = cashflows / (1 + ytm) ** times
    weights = pv / pv.sum()
    return np.sum(weights * times) / (1 + ytm)
