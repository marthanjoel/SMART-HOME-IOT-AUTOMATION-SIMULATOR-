import Device

class AutomationSystem:
    """
    A class representing an automation system.
    """
    def __init__(self):
        self.devices=[]
        self.motion_detected = False
    def add_device(self, device):
        """Adds a device to the automation system."""
        self.devices.append(device)
    def discover_devices(self, device):
        """
        Discovers a new device and adds it to the automation system.

        Args:
        - device : The device to be discovered.

        Returns:
        - True if the device is successfully discovered and added to the system, False otherwise.
        """
        if isinstance(device, Device.Device):
            print("Discovered a new device: ", device.device_id)
            return True
            # self.add_device(device)
    
    def automatic_light_on(self):
        """
        Turns on the smart light if motion is detected and the brightness level is low.
        """
        for device in self.devices:
            if isinstance(device, Device.SecurityCamera):
                for each in self.devices:
                    if isinstance(each, Device.SmartLight) and each.status and int(each.brightness) <=20:
                        each.set_brightness(70)
