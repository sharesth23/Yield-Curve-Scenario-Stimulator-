import numpy as np

def pnl_attribution(dv01, convexity, dy):
    level = dv01 * dy
    curvature = 0.5 * convexity * dy**2
    return {
        "level_pnl": level,
        "convexity_pnl": curvature,
        "total_pnl": level + curvature
    }
