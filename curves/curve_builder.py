import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

class YieldCurve:
    def __init__(self, maturities, yields):
        self.maturities = np.array(maturities)
        self.yields = np.array(yields)

    def interpolate(self):
        return interp1d(self.maturities, self.yields, kind="cubic", fill_value="extrapolate")
