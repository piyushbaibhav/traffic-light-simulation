import tkinter as tk
from tkinter import ttk

# Function to toggle a signal's color
def toggle_signal(signal_index):
    if signal_colors[signal_index] == "red":
        signal_colors[signal_index] = "green"
    else:
        signal_colors[signal_index] = "red"
    update_signals()

# Function to update signal display
def update_signals():
    canvas.delete("signal")  
    for i, color in enumerate(signal_colors):
        x, y = signal_coordinates[i]
        canvas.create_oval(x, y, x + 20, y + 20, fill=color, tags="signal")

# Function to execute the signal sequence
def execute():
    execution_delay = int(execution_delay_entry.get())
    duration = int(duration_entry.get())
    green_signal = int(green_signal_choice.get()) - 1

    # Set the chosen signal to green and others to red
    signal_colors[green_signal] = "green"
    update_signals()

    # After the execution delay, set all signals back to red
    root.after(execution_delay * 1000, set_signals_red)

    # After the execution delay + duration, reset all signals to red
    root.after((execution_delay + duration) * 1000, reset_signals)

# Function to reset all signals to red
def reset_signals():
    for i in range(4):
        signal_colors[i] = "red"
    update_signals()

# Initialize the tkinter window
root = tk.Tk()
root.title("Manual Traffic Signals at Crossroad")

# Create a frame for signal buttons
signal_frame = ttk.Frame(root)
signal_frame.pack()

# Create a canvas for signal display
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.create_rectangle(100, 50, 400, 350, fill="gray")
canvas.create_line(250, 50, 250, 350, fill="white", width=15)
canvas.create_line(100, 200, 400, 200, fill="white", width=15)

# Initialize signal colors
signal_colors = ["red", "red", "red", "red"]

# Store signal coordinates
signal_coordinates = [(240, 150), (240, 230), (200, 190), (280, 190)]

# Create signal toggle buttons with themed styling
signal_buttons = []
for i in range(4):
    button = ttk.Button(signal_frame, text=f"Toggle Signal {i + 1}", command=lambda i=i: toggle_signal(i))
    button.pack(side=tk.LEFT, padx=10, pady=5)
    signal_buttons.append(button)

# Create a dropdown to choose the green signal with themed styling
green_signal_label = ttk.Label(root, text="Select Green Signal:")
green_signal_label.pack()
green_signal_choice = tk.StringVar(root)
green_signal_choice.set("1")
green_signal_menu = ttk.Combobox(root, textvariable=green_signal_choice, values=["1", "2", "3", "4"])
green_signal_menu.pack(padx=10, pady=5)

# Create input fields for execution delay and duration with themed styling
execution_delay_label = ttk.Label(root, text="Execution Delay (seconds):")
execution_delay_label.pack()
execution_delay_entry = ttk.Entry(root)
execution_delay_entry.pack()
duration_label = ttk.Label(root, text="Duration (seconds):")
duration_label.pack()
duration_entry = ttk.Entry(root)
duration_entry.pack()

# Create buttons for execution and reset with themed styling
execute_button = ttk.Button(root, text="Execute", command=execute)
execute_button.pack(padx=10, pady=5)
reset_button = ttk.Button(root, text="ABORT!!!", command=reset_signals)
reset_button.pack(padx=10, pady=5)

# Update signal display
update_signals()

# Start the tkinter main loop
root.mainloop()
