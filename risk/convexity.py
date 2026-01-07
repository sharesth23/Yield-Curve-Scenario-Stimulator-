def convexity(cashflows, ytm, times):
    pv = cashflows / (1 + ytm) ** times
    weights = pv / pv.sum()
    return sum(weights * times * (times + 1))
