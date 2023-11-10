import Device, data_generate

import tkinter as tk
from tkinter import ttk, Text
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

import threading

class Simulator(tk.Tk):
    def __init__(self, automation_system, generator):
        super().__init__()
        self.automation_system = automation_system
        self.automation_toggle = False
        self.generator = generator
        self.create_gui()

    def create_gui(self):
        self.title('Smart Home Simulator')
        self.geometry('800x900')
        self.resizable(0,0)
        self.body = ttk.Frame(self)
        self.body.grid()
        self.automation_button = ttk.Button(
            self.body, 
            text= 'AUTOMATION ON/OFF',
            command = self.automation_check
        )

        self.automation_button.grid()
        self.automation_label = ttk.Label(
            self.body, 
            text='Automation Status: ' + ('ON' if self.automation_toggle else 'OFF')  
        )
        self.automation_label.grid()
        
        self.text = Text(self.body, height=5)
        self.text.grid()
        for device in self.automation_system.devices[::-1]:
            self.text.insert('1.0',device.device_id + ': ' + device.__class__.__name__+ ' Status: ' + ('ON' if device.status else 'OFF')+'\n')
        self.labels=[]
        self.sliders=[]
        for index, device in enumerate(self.automation_system.devices):
            self.space_label = ttk.Label(
                self.body, 
                text=' '
            )
            self.device_label = ttk.Label(
                self.body, 
                text=device.device_id + ' ' + self.wording(device)
            )
            self.space_label.grid()
            self.device_label.grid()
            self.current_val = tk.IntVar()
            
            self.slider = self.slider_decider(device=device)
            self.sliders.append(self.slider)
            # self.slider_enable_disable(device,index)
            self.button = tk.Button(
                self.body,
                text='TOGGLE ON/OFF',
                command = lambda device= device: self.toggle_device(device)
            )
            self.indicator = tk.Label(
                self.body,
                text = self.display_device_curr_readings(device, slider = self.slider)
            )
            self.labels.append(self.indicator)
            self.indicator.grid()
            self.slider.grid()
            self.button.grid()
        self.automation_rule = ttk.Label(
                self.body, 
                text='Automation Rule: Turn on lights when motion is detected'
        )
        self.brightness_label = ttk.Label(
                self.body, 
                text='Brightness events'
        )
        self.brightness_real_time = Text(self.body, height=9)
        
        self.automation_rule.grid()
        self.brightness_label.grid()
        self.automation_label.grid()
        self.brightness_real_time.grid()
        
    
    def display_device_curr_readings(self, device, slider=None, curr_val=None):
        cls_name = device.__class__.__name__
        if cls_name == 'SmartLight':
            return device.device_id + ': ' + str(slider.get()) + '%' if slider else device.device_id + ': ' + curr_val + '%'
        elif cls_name == 'Thermostat':
            return device.device_id + ': ' + str(slider.get()) + 'C' if slider else device.device_id + ': ' + curr_val + 'C'
        return device.device_id + ' - Motion: ' + ('YES' if self.automation_system.motion_detected else 'NO')

    def toggle_device(self, device):
        device.status = not device.status
        self.turn_on_lights_automatically_for_toggle(device)
        self.text.delete('1.0', tk.END)
        for device in self.automation_system.devices[::-1]:
            self.text.insert('1.0', device.device_id + ': ' + device.__class__.__name__+ ' Status: ' + ('ON' if device.status else 'OFF')+'\n')

    def slider_decider(self, device):
        cls_name= device.__class__.__name__
        if cls_name == 'SmartLight':
            return tk.Scale(
                self.body,
                from_=0,
                to=100,
                orient='horizontal', 
                # command=lambda val: self.light_slider_changed(device, current_value),
                command= lambda v, device=device: self.slider_changed(device, v),
                # variable=current_value
            )
        elif cls_name == 'Thermostat':
            return tk.Scale(
                self.body,
                from_=-20,
                to=30,
                orient='horizontal',
                command=lambda v, device=device: self.slider_changed(device, v),
                # variable=current_value
            )
        else: 
           return tk.Button(
                self.body,
                text='Motion setter',
                command = lambda device=device: self.turn_on_lights_automatically(device)
            )

    def turn_on_lights_automatically(self, device):
        self.automation_system.motion_detected = not self.automation_system.motion_detected
        index = self.automation_system.devices.index(device)
        if not self.automation_system.motion_detected:
            self.labels[index].config(text=device.device_id + ' - Motion: ' + ('YES' if self.automation_system.motion_detected else 'NO'))
        else:
            self.automatic_light_updater()
            self.labels[index].config(text=device.device_id + ' - Motion: ' + ('YES' if self.automation_system.motion_detected else 'NO'))

    def automatic_light_updater(self):
        self.automation_system.automatic_light_on()
        for index, each in enumerate(self.automation_system.devices):
            if isinstance(each, Device.SmartLight):
                self.labels[index].config(text= each.device_id + ': ' + str(each.brightness) + '%')
                self.sliders[index].set(each.brightness)

    def turn_on_lights_automatically_for_toggle(self, device):
        if self.automation_system.motion_detected:
            self.automatic_light_updater()

    def slider_enable_disable(self, device, index):
        if not device.status:
            self.sliders[index].config(state=tk.DISABLED)
        else:
            self.slider[index].config(state=tk.NORMAL)

    def automation_check(self):
        if self.automation_toggle:
            self.automation_toggle = False
            self.set_state(self.body, 'normal')
            if self.generator.running:
                generator.stop()
        else:
            self.automation_toggle = True

            threading.Thread(target=generator.start, args=(self.brightness_real_time,)).start()
            self.set_state(self.body, 'disabled', [self.automation_button.winfo_name(), self.brightness_real_time.winfo_name()])

        self.automation_label.config(text='Automation Status: ' + ('ON' if self.automation_toggle else 'OFF'))

    def wording(self, device):
        cls_name= device.__class__.__name__
        if cls_name == 'SmartLight':
            return 'Brightness'
        elif cls_name == 'Thermostat':
            return 'Temperature'
        else: 
            return 'Motion Detection'

    def slider_changed(self, device, current_value):
        index = self.automation_system.devices.index(device)
        self.labels[index].config(text = self.display_device_curr_readings(device, curr_val=current_value))
        cls_name= device.__class__.__name__
        if cls_name == 'SmartLight':
            device.set_brightness(current_value)
        elif cls_name == 'Thermostat':
            device.set_temperature(current_value)
        
    def set_state(self, parent, state='disabled', exclude_names=[]):
        for child in parent.winfo_children():
            if child.winfo_name() not in exclude_names:
                if child.winfo_children():
                    set_state(child, state=state, exclude_names=exclude_names)
                else:
                    try:
                        child.configure(state=state)
                    except tk.TclError:
                        pass

if __name__ == '__main__':
    automation_system= Device.AutomationSystem()
    generator = data_generate.DataGenerator()

    living_room_light= Device.SmartLight('Living Room Light')
    living_room_thermostat= Device.Thermostat('Living Room Thermostat')
    front_door_camera= Device.SecurityCamera('Front door camera')
    # bedroom_light= Device.SmartLight('Bedroom Light')

    undiscovered_devices=[living_room_light, living_room_thermostat, front_door_camera]
    
    for device in undiscovered_devices:
        if automation_system.discover_devices(device):
            automation_system.add_device(device)
    
    gui = Simulator(automation_system, generator)
    gui.mainloop()