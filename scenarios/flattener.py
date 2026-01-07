def flattener(yields, maturities, bp=25):
    shock = (1 - maturities / maturities.max()) * (bp / 10000)
    return yields - shock
