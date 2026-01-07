import matplotlib.pyplot as plt

def plot_curves(maturity, base, shocked):
    plt.plot(maturity, base, label="Base")
    plt.plot(maturity, shocked, label="Scenario")
    plt.legend()
    plt.grid()
    plt.show()
