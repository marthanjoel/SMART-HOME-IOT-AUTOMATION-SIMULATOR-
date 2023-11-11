import random

class Device:
    def __init__(self, device_id_, status = False):
        self.device_id=device_id_
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
    def __init__(self, device_id, security_status = False):
        super().__init__(device_id)
        self.security_status = security_status
   
    def set_security_status(self, security_status):
        self.security_status = security_status 
  

class AutomationSystem:
    def __init__(self):
        self.devices=[]
        self.motion_detected = False
    def add_device(self, device):
        self.devices.append(device)
    def discover_devices(self, device):
        if isinstance(device, Device):
            print("Discovered a new device: ", device.device_id)
            return True
            # self.add_device(device)
    
    def automatic_light_on(self):
        for device in self.devices:
            if isinstance(device, SecurityCamera):
                for each in self.devices:
                    if isinstance(each, SmartLight) and each.status and int(each.brightness) <=20:
                        each.set_brightness(70)
