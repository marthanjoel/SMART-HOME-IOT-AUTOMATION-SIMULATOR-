class Device:
    """
    A class representing a device.
    """
    def __init__(self, device_id_, status = False):
        """
        Initializes a Device object.

        Args:
        - device_id: The unique identifier of the device.
        - status: The status of the device, True if on, False if off.
        """
        self.device_id=device_id_
        self.status=status

    def turn_on(self):
        """
        Turns on the device.
        """
        self.status=True
    
    def turn_off(self):
        """
        Turns off the device.
        """
        self.status=False


class SmartLight(Device):
    """
    A class representing a thermostat device.
    """
    def __init__(self, device_id, brightness = 0):
        """
        Initializes a SmartLight object.

        Args:
        - device_id: The unique identifier of the device.
        - brightness: The brightness level of the light.
        """
        super().__init__(device_id)
        self.brightness= brightness

    def set_brightness(self, brightness):
        """
        Sets the brightness level of the light.
        """
        self.brightness=brightness

    

class Thermostat(Device):
    """
    A class representing a thermostat device.
    """
    def __init__(self, device_id, temperature = 0):
        """
        Initializes a Thermostat object.

        Args:
        - device_id: The unique identifier of the device.
        - temperature: The temperature level of the thermostat.
        """
        super().__init__(device_id)
        self.temperature = temperature

    def set_temperature(self, temperature):
        """
        Sets the temperature level of the thermostat.
        """
        self.temperature = temperature    

class SecurityCamera(Device):
    """
    A class representing a security camera device.
    """
    def __init__(self, device_id, security_status = False):
        """
        Initializes a SecurityCamera object.
        """
        super().__init__(device_id)
        self.security_status = security_status
   
    def set_security_status(self, security_status):
        """
        Sets the security status of the camera.
        """
        self.security_status = security_status 
  