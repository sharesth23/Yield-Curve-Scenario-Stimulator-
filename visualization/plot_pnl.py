import matplotlib.pyplot as plt

def plot_pnl(pnl_dict):
    plt.bar(pnl_dict.keys(), pnl_dict.values())
    plt.title("PnL Attribution")
    plt.show()
