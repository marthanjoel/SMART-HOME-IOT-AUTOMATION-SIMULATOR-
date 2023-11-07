# import tkinter as tk
# from tkinter import ttk

# def create_device_frame(container, device_name):
#     frame = ttk.Frame(container)
#     frame.pack(fill='x', padx=5, pady=5)

#     ttk.Label(frame, text=device_name).grid(column=0, row=0, sticky='w')
#     ttk.Checkbutton(frame, text="On/Off").grid(column=1, row=0)
#     ttk.Scale(frame, from_=0, to=100, orient='horizontal').grid(column=2, row=0)

#     return frame

# def create_app():
#     root = tk.Tk()
#     root.title("Smart Home IoT Simulator")

#     mainframe = ttk.Frame(root, padding="10")
#     mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

#     create_device_frame(mainframe, "Living Room Light")
#     create_device_frame(mainframe, "Living Room Thermostat")
#     create_device_frame(mainframe, "Front Door Camera")

#     root.mainloop()

# if __name__ == "__main__":
#     create_app()

import tkinter as tk

def show_value(val):
    label.config(text = f"Current Value: {val}")

root = tk.Tk()
root.geometry("300x200")

# Create a slider
slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=lambda val: show_value(val))
slider.pack()

# Create a label to display the current value
label = tk.Label(root, text="")
label.pack()

root.mainloop()