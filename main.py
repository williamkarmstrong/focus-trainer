import os
import numpy as np
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLOTS = os.path.join(ROOT, "plots")

SAVE = True

def plot(time, sig, filename):
    pass

def save_svg(fig, filename):
    if SAVE:
        os.makedirs(PLOTS, exist_ok=True)
        fig.savefig(os.path.join(PLOTS, filename + ".svg"))

if __name__ == "__main__":
    pass