import pandas as pd
from scenarios.steepener import steepener
from visualization.plot_curves import plot_curves

df = pd.read_csv("data/gov_yields.csv")
m = df["maturity"].values
y = df["yield"].values

shocked = steepener(y, m)
plot_curves(m, y, shocked)
