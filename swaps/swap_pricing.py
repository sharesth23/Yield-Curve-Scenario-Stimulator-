def swap_pv(fixed_rate, market_rate, notional, maturity):
    return notional * (market_rate - fixed_rate) * maturity
