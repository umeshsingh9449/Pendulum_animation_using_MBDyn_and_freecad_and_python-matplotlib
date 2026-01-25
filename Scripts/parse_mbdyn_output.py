import numpy as np
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE.parent / "outputs"
OUT.mkdir(exist_ok=True)

# Example data
time = np.linspace(0, 60, 1000)
theta = 0.2 * np.cos(time)

np.savez(
    OUT / "pendulum_data.npz",
    time=time,
    theta=theta
)

print("Saved pendulum_data.npz")
