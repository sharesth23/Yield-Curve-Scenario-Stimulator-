import numpy as np

def bond_price(face, coupon, ytm, maturity):
    times = np.arange(1, maturity + 1)
    cashflows = np.full(maturity, face * coupon)
    cashflows[-1] += face
    return np.sum(cashflows / (1 + ytm) ** times)
