import numpy as np
from scipy.interpolate import interp1d

class SwapCurve:
    def __init__(self, tenors, rates):
        self.curve = interp1d(tenors, rates, kind="linear", fill_value="extrapolate")

    def rate(self, t):
        return self.curve(t)
