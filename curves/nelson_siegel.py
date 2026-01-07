import numpy as np

def nelson_siegel(t, beta0, beta1, beta2, tau):
    return (
        beta0
        + beta1 * (1 - np.exp(-t / tau)) / (t / tau)
        + beta2 * ((1 - np.exp(-t / tau)) / (t / tau) - np.exp(-t / tau))
    )
