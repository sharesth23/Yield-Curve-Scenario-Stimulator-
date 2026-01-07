def steepener(yields, maturities, bp=25):
    shock = (maturities / maturities.max()) * (bp / 10000)
    return yields + shock
