# Importing modules
import math
import tkinter as tk

# Creating the main window
root = tk.Tk()
root.title("The Circles and the Polygon • MOZKA")

# Creating the canvas
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Drawing the circle
circle = canvas.create_oval(50, 50, 450, 450, width = 2)

# Initializing the number of sides and the radius of the polygon
n = 3
r = 200

# Calculating the coordinates of the polygon vertices
def polygon_coords(n, r):
    coords = []
    for i in range(n):
        angle = i * 2 * math.pi / n
        x = r * math.cos(angle) + 250
        y = r * math.sin(angle) + 250
        coords.append(x)
        coords.append(y)
    return coords

# Drawing the polygon
polygon = canvas.create_polygon(polygon_coords(n, r), fill="red")

# Creating a label for circumference
circumference_label = tk.Label(root, text=f"Circumference of Polygon: {2 * n * r * math.sin(math.pi / n):.4f}",font=("Arial", 15 ))
circumference_label.pack()

# Creating the slider
slider = tk.Scale(root, from_=3, to=40, orient=tk.HORIZONTAL, label="Number of sides", length=400)
slider.pack(pady=20)

# Updating the polygon and the values of pi and circumference when the slider changes
def update(event):
    global n, polygon
    n = slider.get()
    canvas.delete(polygon)
    polygon = canvas.create_polygon(polygon_coords(n, r), fill="red")
    pi = n * math.sin(math.pi / n)
    circumference = 2 * n * r * math.sin(math.pi / n)
    pi_label.config(text=f"Pi: {pi:.10f}")
    pce_label.config(text=f"% Difference in Pi: {((math.pi - pi)/math.pi*100):.4f}")
    circumference_label.config(text=f"Circumference: {circumference:.4f}")
    area_polygon = 0.5 * n * r**2 * math.sin(2 * math.pi / n)
    area_circle = math.pi * r**2
    percent_diff = abs(area_polygon - area_circle) / area_circle * 100
    area_polygon_label.config(text=f"Area of Polygon: {area_polygon:.4f}")
    area_circle_label.config(text=f"Area of Circle: {area_circle:.4f}")
    percent_diff_label.config(text=f"% Difference in Area: {percent_diff:.4f}")

slider.bind("<B1-Motion>", update)

# Creating a frame for labels
frame = tk.Frame(root)
frame.pack()

# Creating a label for pi
pi_label = tk.Label(frame, text=f"Pi: {n * math.sin(math.pi / n):.10f}", font=("Arial", 20))
pi_label.grid(row=1, column=0)

# Creating a label for percentage error
pce_label = tk.Label(frame, text=f"% Difference in Pi: {((n * math.sin(math.pi / n) / math.pi)*100):.4f}%" ,font=("Arial", 15 ))
pce_label.grid(row=2, column=0)

# Creating a label for actual pi
A_pi_label = tk.Label(frame, text=f"Actual Pi: {math.pi:.11f}" ,font=("Arial", 15 ))
A_pi_label.grid(row=3, column=0)

#column spacing
col_space_label = tk.Label(frame, text="                                    ")
col_space_label.grid(row=1, column=1)

# Creating a label for percentage difference in areas
percent_diff_label = tk.Label(frame, text=f"% Difference in Area: {abs(0.5 * n * r**2 * math.sin(2 * math.pi / n) - math.pi * r**2) / (math.pi * r**2) * 100:.4f}", font=("Arial", 20))
percent_diff_label.grid(row=1, column=2)

# Creating a label for area of polygon
area_polygon_label = tk.Label(frame, text=f"Area of Polygon: {0.5 * n * r**2 * math.sin(2 * math.pi / n):.4f}", font=("Arial", 15))
area_polygon_label.grid(row=2, column=2)

# Creating a label for area of circle
area_circle_label = tk.Label(frame, text=f"Area of Circle: {math.pi * r**2:.4f}", font=("Arial", 15))
area_circle_label.grid(row=3, column=2)

# Creating a label for area of circle
company_label = tk.Label(root, text="A project by MOZKA • 2019-Present", font=("Perpetua Titling MT", 12))
company_label.pack(pady=10)

root.mainloop()