import Device

import tkinter as tk
from tkinter import ttk, Text
from tkinter.scrolledtext import ScrolledText

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

class Simulator(tk.Tk):
    def __init__(self, automation_system):
        super().__init__()
        self.automation_system = automation_system
        self.automation_toggle = False
        self.create_gui()

    def create_gui(self):
        self.title('Smart Home Simulator')
        self.geometry('800x900')
        self.resizable(0,0)
        self.body = ttk.Frame(self)
        self.body.grid()
        # self.body.columnconfigure(0, weight=1)
        # self.body.columnconfigure(1, weight=3)
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
        
        # st = ScrolledText(self.body, width=60, height=30)
        # st.grid(fill=tk.BOTH, side=tk.LEFT, expand=True)
        # for device in self.devices:
        #     st.insert(device.device_id + ': ' + device.__class__.__name__+ 'Status' + device.status)
        
        self.text = Text(self.body, height=8)
        self.text.grid()
        for device in self.automation_system.devices[::-1]:
            self.text.insert('1.0',device.device_id + ': ' + device.__class__.__name__+ ' Status: ' + str(device.status)+'\n')
        self.labels=[]
        for device in self.automation_system.devices:
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
            
            # self.slider = ttk.Scale(
            #     self.body,
            #     from_=0,
            #     to=100,
            #     orient='horizontal',  # vertical
            #     command=lambda val: self.light_slider_changed(device, val),
            #     variable=self.current_val
            # )

            # self.slider_value = ttk.Label(
            #     self.body, 
            #     text= ''  
            # )
            # self.slider_value.grid()
            self.button = tk.Button(
                self.body,
                text='TOGGLE ON/OFF',
                command = lambda device= device: self.toggle_device(device)
            )
            self.indicator = tk.Label(
                self.body,
                text = self.indic(device, slider = self.slider)
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
        self.automation_rule.grid()
        self.brightness_label.grid()
        self.automation_label.grid()
    
    def indic(self, device, slider=None, curr_val=None):
        cls_name = device.__class__.__name__
        if cls_name == 'SmartLight':
            return device.device_id + ': ' + str(slider.get()) + '%' if slider else device.device_id + ': ' + curr_val + '%'
        elif cls_name == 'Thermostat':
            return device.device_id + ': ' + str(slider.get()) + '%' if slider else device.device_id + ': ' + curr_val + '%'
        return device.device_id + ' - Motion: ' + str(slider.get()) 

    def toggle_device(self, device):
        device.status = not device.status
        self.text.delete('1.0', tk.END)
        for device in self.automation_system.devices[::-1]:
            self.text.insert('1.0', device.device_id + ': ' + device.__class__.__name__+ ' Status: ' + str(device.status)+'\n')
        

    def slider_decider(self, device):
        cls_name= device.__class__.__name__
        if cls_name == 'SmartLight':
            return tk.Scale(
                self.body,
                from_=0,
                to=100,
                orient='horizontal',  # vertical
                # command=lambda val: self.light_slider_changed(device, current_value),
                command= lambda v, device=device: self.slider_changed(device, v),
                # variable=current_value
            )
        elif cls_name == 'Thermostat':
            return tk.Scale(
                self.body,
                from_=-20,
                to=30,
                orient='horizontal',  # vertical
                command=lambda v, device=device: self.slider_changed(device, v),
                # variable=current_value
            )
        else: 
           return tk.Scale(
                self.body,
                from_=-20,
                to=30,
                orient='horizontal',  # vertical
                # command=slider_changed,
                # variable=current_value
            )

    def automation_check(self):
        # print('clicked')
        if self.automation_toggle:
            self.automation_toggle = False
            # Turn off data generator thread
        else:
            self.automation_toggle = True
            # Start the data generator thread
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
        # print('a')
        index = self.automation_system.devices.index(device)
        self.labels[index].config(text = self.indic(device, curr_val=current_value))
        cls_name= device.__class__.__name__
        if cls_name == 'SmartLight':
            device.set_brightness(current_value)
        elif cls_name == 'Thermostat':
            device.set_temperature(current_value)
        
        # self.slider_value.configure(text = current_value)

    # def indic2(self, device, current_val):
    #     cls_name= device.__class__.__name__
    #     if cls_name == 'SmartLight':
    #         return device.device_id + ': ' + current_val + '%'
    #     elif cls_name == 'Thermostat':
    #         return device.device_id + ': ' + current_val + 'C'
    #     return device.device_id + ' - Motion: ' + current_val 

    

if __name__ == '__main__':
    living_room_light= Device.SmartLight('Living Room Light')
    living_room_thermostat= Device.Thermostat('Living Room Thermostat')
    front_door_camera= Device.SecurityCamera('Front door camera')
    undiscovered_devices=[living_room_light, living_room_thermostat, front_door_camera]
    automation_system= Device.AutomationSystem()
    for device in undiscovered_devices:
        if automation_system.discover_devices:
            automation_system.add_devices(device)
    gui = Simulator(automation_system)
    gui.mainloop()