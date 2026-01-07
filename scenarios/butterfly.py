import numpy as np

def butterfly(yields, maturities, bp=20):
    center = maturities.mean()
    shock = -((maturities - center) ** 2) / center**2
    shock = shock / shock.min() * (bp / 10000)
    return yields + shock
