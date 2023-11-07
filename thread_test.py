import tkinter as tk
import threading
import time

class DataGenerator:
    def __init__(self):
        self.running = False
        self.data = []

    def start(self):
        self.running = True
        while self.running:
            # Generate some data
            new_data = "New data\n"
            self.data.append(new_data)
            
            # Update the Text widget and write to file
            text.insert(tk.END, new_data)
            with open("data.txt", "a") as file:
                file.write(new_data)
            
            # Sleep for a bit to simulate time-consuming data generation
            time.sleep(1)

    def stop(self):
        self.running = False

def toggle_data_generation():
    if generator.running:
        generator.stop()
    else:
        threading.Thread(target=generator.start).start()

root = tk.Tk()

# Create a Text widget to display the data
text = tk.Text(root)
text.pack()

# Create a button to start and stop the data generation
button = tk.Button(root, text="Start/Stop", command=toggle_data_generation)
button.pack()

# Create a data generator
generator = DataGenerator()

root.mainloop()
