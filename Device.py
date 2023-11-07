import random

class Device:
    def __init__(self, device_id, status = False):
        self.device_id=device_id
        self.status=status
    
    def turn_on(self):
        self.status=True
    
    def turn_off(self):
        self.status=False


class SmartLight(Device):
    def __init__(self, device_id, brightness = 0):
        super().__init__(device_id)
        self.brightness= brightness

    def set_brightness(self, brightness):
        self.brightness=brightness

    

class Thermostat(Device):
    def __init__(self, device_id, temperature = 0):
        super().__init__(device_id)
        self.temperature = temperature

    def set_temperature(self, temperature):
        self.temperature = temperature    

class SecurityCamera(Device):
    def __init__(self, device_id, motion_detected = False):
        super().__init__(device_id)
        self.motion_detected = motion_detected
    
    def set_motion_detected(self, motion_detected):
        self.motion_detected = motion_detected  

class AutomationSystem:
    def __init__(self):
        self.devices=[]
    def add_devices(self, device):
        self.devices.append(device)
    def discover_devices(self, devices):
        for device in devices:
            if device.isinstance(Device):
                print("Discovered a new device: ", device.device_id)
                # self.add_devices(device)
    
    def execute_tasks(self):
        for device in self.devices:
            if isinstance(device, SmartLight):
                device.set_brightness(random.randint(0, 100))
            elif isinstance(device, Thermostat):
                device.set_temperature(random.randint(15, 30))
            elif isinstance(device, SecurityCamera):
                device.set_security_status(bool(random.getrandbits(1)))