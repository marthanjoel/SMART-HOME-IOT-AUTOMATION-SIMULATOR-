import unittest
from tkinter import *
import test_tkinter, Device


class TestSimulator(unittest.TestCase):
    def setUp(self):
        self.automation_system = test_tkinter.automation_system
        self.generator = test_tkinter.data_generate
        self.living_room_light= Device.SmartLight('Living Room Light')
        self.living_room_thermostat= Device.Thermostat('Living Room Thermostat')
        self.front_door_camera= Device.SecurityCamera('Front door camera')

        undiscovered_devices=[self.living_room_light, self.living_room_thermostat, self.front_door_camera]

        for device in undiscovered_devices:
            if self.automation_system.discover_devices(device):
                self.automation_system.add_device(device)

        self.simulator = Simulator(automation_system, generator)


    def test_toggle_device(self):
        self.simulator.toggle_device(living_room_light)
        self.assertEqual(living_room_light.status, True)

    def test_slider_decider(self):
        self.assertIsInstance(self.simulator.slider_decider(living_room_light), Scale)

    def test_wording(self):
        self.assertEqual(self.simulator.wording(living_room_light), 'Brightness')

    def test_display_device_curr_readings(self):
        self.assertEqual(self.simulator.display_device_curr_readings(living_room_light), 'Living Room Light: 0%')

    def test_slider_changed(self):
        self.simulator.slider_changed(living_room_light, 50)
        self.assertEqual(self.simulator.display_device_curr_readings(living_room_light), 'Living Room Light: 50%')

    def test_set_state(self):
        self.simulator.set_state(self.simulator.body, state='disabled')
        self.assertEqual(self.simulator.body['state'], 'disabled')

    if __name__ == '__main__':
        unittest.main(argv=[''], exit=False)
    self.brightness_real_time = Text(self.body, height=9)