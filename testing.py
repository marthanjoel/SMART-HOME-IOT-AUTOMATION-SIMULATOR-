import unittest
from tkinter import *
import Simulator, Device, data_generate, Automation_system


class TestSimulator(unittest.TestCase):
    def setUp(self):
        self.automation_system = Automation_system.AutomationSystem()
        self.generator = data_generate.DataGenerator()
        self.living_room_light= Device.SmartLight('Living Room Light')
        self.living_room_thermostat= Device.Thermostat('Living Room Thermostat')
        self.front_door_camera= Device.SecurityCamera('Front door camera')

        undiscovered_devices=[self.living_room_light, self.living_room_thermostat, self.front_door_camera]

        for device in undiscovered_devices:
            if self.automation_system.discover_devices(device):
                self.automation_system.add_device(device)

        self.simulator = Simulator.Simulator(self.automation_system, self.generator)

    def test_initial_state_of_devices(self):
        self.assertEqual(self.living_room_light.status, False)
        self.assertEqual(self.living_room_thermostat.status, False)
        self.assertEqual(self.front_door_camera.status, False)
        self.assertEqual(self.living_room_light.brightness, 0)
        self.assertEqual(self.living_room_thermostat.temperature, 0)
        self.assertEqual(self.front_door_camera.security_status, False)
        self.assertEqual(self.automation_system.motion_detected, False)
    
    def test_automation_system_setup(self):
        self.assertEqual(self.simulator.automation_system.motion_detected, False)
        self.assertEqual(len(self.simulator.automation_system.devices), 3)
        self.assertEqual(self.simulator.automation_system.devices[0].__class__.__name__, 'SmartLight')
        self.assertEqual(self.simulator.automation_system.devices[1].__class__.__name__, 'Thermostat')
        self.assertEqual(self.simulator.automation_system.devices[2].__class__.__name__, 'SecurityCamera')

    def test_living_room_light_status_button(self):
        self.simulator.buttons[0].invoke()
        self.assertEqual(self.simulator.automation_system.devices[0].status, True)
        self.simulator.buttons[0].invoke()
        self.assertEqual(self.simulator.automation_system.devices[0].status, False)
        

    def test_living_room_thermostat_status_button(self):
        self.simulator.buttons[1].invoke()
        self.assertEqual(self.simulator.automation_system.devices[1].status, True)
        self.simulator.buttons[1].invoke()
        self.assertEqual(self.simulator.automation_system.devices[1].status, False)
        

    def test_front_door_camera_status_button(self):
        self.simulator.buttons[2].invoke()
        self.assertEqual(self.simulator.automation_system.devices[2].status, True)
        self.simulator.buttons[2].invoke()
        self.assertEqual(self.simulator.automation_system.devices[2].status, False)
        

    def test_automation_toggle_button(self):
        self.simulator.automation_button.invoke()
        self.assertEqual(self.simulator.automation_toggle, True)
        self.simulator.automation_button.invoke()
        self.assertEqual(self.simulator.automation_toggle, False)
        
    def test_living_room_light_slider(self):
        self.simulator.sliders[0].set(0)
        self.assertEqual(self.simulator.automation_system.devices[0].brightness, 0)
        self.simulator.sliders[0].set(20)
        self.assertEqual(self.simulator.sliders[0].get(), 20)

    def test_living_room_thermostat_slider(self):
        self.simulator.sliders[1].set(0)
        self.assertEqual(self.simulator.automation_system.devices[1].temperature, 0)
        self.simulator.sliders[1].set(20)
        self.assertEqual(self.simulator.sliders[1].get(), 20)
 
    def test_front_door_camera_motion_button(self):
        self.simulator.sliders[2].invoke()
        self.assertEqual(self.simulator.automation_system.motion_detected, True)
        self.simulator.sliders[2].invoke()
        self.assertEqual(self.simulator.automation_system.motion_detected, False)
        
    def test_automatic_light_adjusting_when_motion_detected(self):
        self.assertEqual(self.simulator.automation_system.devices[0].brightness, 0)
        self.simulator.buttons[0].invoke()
        self.simulator.sliders[2].invoke()
        self.assertEqual(self.simulator.automation_system.devices[0].brightness, 70)
        self.assertEqual(self.simulator.sliders[0].get(), 70)
