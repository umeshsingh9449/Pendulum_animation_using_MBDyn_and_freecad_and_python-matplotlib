from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# Absolute path to this script
SCRIPT_DIR = Path(__file__).resolve().parent

# Absolute path to outputs
DATA_FILE = SCRIPT_DIR.parent / "outputs" / "pendulum_data.npz"

print("Looking for file at:")
print(DATA_FILE)

if not DATA_FILE.exists():
    raise FileNotFoundError(f"File not found: {DATA_FILE}")

data = np.load(DATA_FILE)

plt.plot(data["time"], data["theta"])
plt.xlabel("Time (s)")
plt.ylabel("Theta (rad)")
plt.grid()

out_dir = SCRIPT_DIR.parent / "outputs"
out_dir.mkdir(exist_ok=True)

plt.savefig(out_dir / "theta_vs_time.png", dpi=150)
plt.close()

print("Saved plot to outputs/theta_vs_time.png")


