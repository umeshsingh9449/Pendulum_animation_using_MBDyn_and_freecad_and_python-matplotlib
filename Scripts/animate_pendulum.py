from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#--------------paths----------------

Script_Dir = Path(__file__).resolve().parent
Data_File = Script_Dir.parent / "outputs" / "pendulum_data.npz"
Out_Dir = Script_Dir.parent /"outputs"
Out_Dir.mkdir(exist_ok=True)

Video_file = Out_Dir / "pendulum.mp4"

#---------------Load data-------------

data = np.load(Data_File)
time = data["time"]
theta = data["theta"]

#-----------Pendulum Parameters---------
L=1.0 #length in meters
x = L * np.sin(theta)
y = -L *np.cos(theta)

#----------Figure Setup-----------------
fig, ax = plt.subplots()
ax.set_xlim(-1.2 * L, 1.2*L)
ax.set_ylim(-1.2*L, 0.2 * L)
ax.set_aspect("equal")
ax.grid()

line, = ax.plot([], [], "o-", lw=2)
time_text = ax.text(0.05, 0.9, "", transform=ax.transAxes)

#------------------Animation Functions--------
def init():
    line.set_data([],[])
    time_text.set_text("")
    return line, time_text

def update(i):
    line.set_data([0, x[i]], [0,y[i]])
    time_text.set_text(f"t = {time[i]:.2f} s")
    return line, time_text

#--------------Create animation----------------

anim = FuncAnimation(
    fig,
    update,
    frames=len(time),
    init_func=init,
    blit=True,
    interval=1000 * (time[1] - time[0])
)

#------------Save Video-----------------------
print("saving Video...")
anim.save(Video_file, writer="ffmpeg", dpi=150)
plt.close()

print(f" Animation saved to {Video_file}")