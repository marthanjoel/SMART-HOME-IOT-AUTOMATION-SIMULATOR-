import random
import datetime
import tkinter as tk
import time

class DataGenerator:
    def __init__(self):
        self.running = False
        self.data = []

    def start(self, text):
        self.running = True
        while self.running:
            new_data = self.generate_data()
            self.data.append(new_data)
            
            text.insert(tk.END, new_data)
            with open("sensor_data.txt", "a") as file:
                file.write(new_data)
            
            time.sleep(1)

    def generate_data(self):
        now = datetime.datetime.now()
        timestamp = now.strftime("[%Y-%m-%d %H:%M:%S]")
        brightness = random.randint(0, 100)
        data = f"{timestamp} Living Room Light brightness set to {brightness}%\n"
        return data

    def stop(self):
        self.running = False