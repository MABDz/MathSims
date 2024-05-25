#import pyi_splash
import tkinter as tk
import matplotlib
import matplotlib.patches as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import numpy as np

#pyi_splash.close()

G = 6.674 * 10**-11

mass_e = 5.972 * 10**24 
mass_c = 1

radius_e = 6.371 * 10**6

height_m = radius_e + 2.5 * 10**6

v0 = 100

pos = np.array([0, height_m, 0])

delta_t = 10

iterations = 10000

state = 'normal'

ecc = 0



def update_velocity_position(pos, v):
    global mass_c
    
    r = np.linalg.norm(pos)
    if r <= radius_e:
        return pos, v

    uv_r = pos / r
    fg = (-G * mass_e * mass_c) * uv_r / r**2

    delta_m = fg * delta_t
    v = v + (delta_m)/mass_c
    pos = pos + v * delta_t

    return pos, v

def plot_orbit(v0):
    global e
    
    pos = np.array([0, height_m, 0])
    v = np.array([v0, 0, 0])

    positions = [pos]
    distances = [np.linalg.norm(pos)]

    for _ in range(iterations):  
        pos, v = update_velocity_position(pos, v)
        positions.append(pos)
        distances.append(np.linalg.norm(pos))

    positions = np.array(positions)
    
    major_a = max(distances)
    minor_a = min(distances)


    ecc = np.sqrt(1 - (minor_a**2 / major_a**2))
    
    e_label.config(text=f"Eccentricity: ~{ecc:.3f}")

    if ecc < 0.2:
        color = 'red'
    else:
        color = '#1f77b4'

    ax.clear()
    earth = plt.Circle((0, 0), radius_e, color='#45b592')  # Add Earth
    ax.add_artist(earth)
    ax.plot(positions[:, 0], positions[:, 1], color=color)
    ax.set_xlim(-11**7, 11**7)
    ax.set_ylim(-11**7, 11**7)
    ax.set_xlabel("Distance")
    canvas.draw()
    
def on_button_click():
    global v0, iterations, mass_c, state
    v0 = float(entryv.get())
    iterations = int(entryi.get())
    # mass_c = int(entrym.get())
    state = 'disabled'
    plot_orbit(v0)


def on_slider_change_v(val):
    global v0
    v0 = val
    plot_orbit(float(val))

def on_slider_change_m(val):
    global mass_c
    mass_c = int(val)
    plot_orbit(float(v0))
    
def on_slider_change_i(val):
    global iterations 
    iterations = int(val)
    plot_orbit(float(v0))

root = tk.Tk()
root.resizable(False, False)
root.title("Newton's Cannonball • MOZKA 2023")

fig = Figure(figsize=(5, 5))
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

e_label = tk.Label(root, text=f"Ecentricity of orbit: {ecc}")
e_label.pack(fill=tk.X)

s_button = tk.Button(root, text="Click to plot orbit for large values", 
                     bg='#45b592', 
                     fg='#ffffff', 
                     borderwidth=0, 
                     command=on_button_click)
s_button.pack(fill=tk.X)

slider_v = tk.Scale(root, from_=500, to=10000, resolution= 100, 
                    orient=tk.HORIZONTAL,
                    label="Initial speed", 
                    command=on_slider_change_v,
                    state=state)
slider_v.pack(fill=tk.X)

entryv = tk.Entry(root, 
                  bg='#45b592', 
                  fg='#ffffff')
entryv.insert(0,"Add large initial velocities here")
entryv.pack(fill=tk.X)

# slider_m = tk.Scale(root, from_=1, to=1000, resolution= 10, 
#                     orient=tk.HORIZONTAL,
#                     label="Mass of cannonball", 
#                     command=on_slider_change_m,
#                     state=state)
# slider_m.pack(fill=tk.X)

# entrym = tk.Entry(root, bg='#45b592', fg='#ffffff')
# entrym.insert(0,"Add large masses here")
# entrym.pack(fill=tk.X)

slider_i = tk.Scale(root, from_=1000, to=50000, resolution= 100, 
                    orient=tk.HORIZONTAL,
                    label="Simulation Iterations", 
                    command=on_slider_change_i,
                    state=state)
slider_i.pack(fill=tk.X)

entryi = tk.Entry(root, bg='#45b592', fg='#ffffff' )
entryi.insert(0,"Add large iteration counts here")
entryi.pack(fill=tk.X)



plot_orbit(v0)

tk.mainloop()
