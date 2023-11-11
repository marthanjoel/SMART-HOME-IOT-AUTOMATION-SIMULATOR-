# Smart Home IoT Automation Simulator Project

This project is a Smart Home IoT Automation Simulator built using Tkinter in Python. The simulator allows users to control various smart devices in a home, such as lights, thermostats, and security systems.

## Installation

To run the simulator, you will need to have Python 3 installed on your computer. You can download Python 3 from the official website: https://www.python.org/downloads/

Once you have Python 3 installed, you can clone this repository and to run the simulator, use the following command to the terminal `python simulator.py`. 

## Usage

The simulator provides a graphical user interface (GUI) that allows users to interact with various smart devices in a home. Users can turn lights on and off, adjust the temperature of the thermostat, and arm or disarm the security system.
The automation system is embedded to the project which activate lights to 70% automatically when motion is detected. Also if randomization mechanism is turned on, it will simulate a brightness of lights for automatic configuration and gathers sensor data and storing it in a file for future analysis.

## Testing

Project is tested with **unittest**. Test cases to ensure that the simulator and automation system behave as expected are written. To run the tests, the following command should be entered to the terminal `python -m unittest testing -v`

## Documentation and instructions

Each class and methods have their own description and explanations written above them. When you run the project, a window appears as a simulator board for the Smart Home IoT Automation project. To toggle the randomization mechanism, use **Automation ON/OFF** button and its state is displayed right below. Each device's status and types are displayed in the text area. Below that, each device has their status toggle button **TOGGLE ON/OFF** and their respective slider or button to set their properties and label to view their properties. 

If the randomization mechanism is turned on, a simulation for brightness of lights are randomly generated every second in the text area named **Brightness events**. During the generation, every widgets except the randomization mechanism button and last text area are disabled.

UML
