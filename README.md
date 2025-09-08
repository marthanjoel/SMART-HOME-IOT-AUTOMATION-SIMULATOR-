# Smart Home IoT Automation Simulator Project

This project is a **Smart Home IoT Automation Simulator** built using **Tkinter in Python**.  
It demonstrates how IoT devices such as **lights, thermostats, and security systems** can be controlled and automated in a smart home environment.

---

## Setup Steps

1. Clone this repository:
git clone https://github.com/marthanjoel/SMART-HOME-IOT-AUTOMATION-SIMULATOR-.git
cd SMART-HOME-IOT-AUTOMATION-SIMULATOR-

-----------------------------------------------------------------------------------

2. Install required Python modules:
pip install -r requirements.txt
-----------------------------------------------------------------------------------


3. On Ubuntu, install Tkinter if missing:
sudo apt install python3-tk -y

------------------------------------------------------------------------------------

4. Run the simulator:
python3 Simulator.py


------------------------------------------------------------------------------------

## Challenges Faced

- Original code used **Windows-only libraries** (`ctypes.windll`) which had to be removed for Ubuntu.  
- **Tkinter not installed by default** → needed `sudo apt install python3-tk`.  
- **Case sensitivity issues** (`Simulator.py` vs `simulator.py`).  
  
- Pushing to GitHub → had to reconfigure **git remote** for personal repository.  

---

## How the Simulation Works

- The simulator launches a **Tkinter GUI** that represents smart home devices.  
- Devices can be controlled manually with **buttons and sliders**.  
- Devices can also communicate via **MQTT messages** when a broker is active.  
- **Automation rules** are included:  
- Example: *If motion is detected, lights automatically turn on to 70% brightness.*  
- A **randomization feature** simulates sensor fluctuations (e.g., brightness events).  
- Device states and automation events are displayed in the text area of the GUI.  

---

## What Sensors or Devices Are Emulated

- **Smart Light (Living Room Light)** → ON/OFF + brightness control  
- **Thermostat** → adjustable temperature  
- **Security Camera** → ON/OFF + motion detection  
- **Motion Sensor** → works with the camera to trigger automation  

---

## Ideas for Future Improvements

- Add new devices (door locks, plugs, humidity sensors, more lights)  
- Replace Tkinter with a **web dashboard** for accessibility  
- Integrate with **cloud IoT platforms** (AWS IoT, HiveMQ, Azure IoT)  
- Add **data logging & analytics** for long-term usage  
- Build a **mobile app** for remote control  
- Improve automation logic (time schedules, conditional rules, multi-device triggers)  





