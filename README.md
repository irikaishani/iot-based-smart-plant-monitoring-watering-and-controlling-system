# 🌿 Smart Plant Health Monitoring and Watering System

An **IoT-based Precision Agriculture Project** that automates plant watering by monitoring **real-time soil moisture, temperature, and humidity**, while offering both **manual and automatic motor control** through a user-friendly **Streamlit dashboard**.

---

## 📌 Project Overview

Traditional irrigation methods waste a lot of water and require constant monitoring. This project addresses these issues by building a **smart, sensor-integrated system** using **Arduino and Streamlit**, which:

- Reads soil moisture, temperature, and humidity using sensors.
- Automatically controls a water pump based on moisture level.
- Allows **manual ON/OFF** control through a web dashboard.
- Displays real-time data and plots historical trends interactively.

---

## ⚙️ Hardware Components

| Component               | Description                                                  |
|------------------------|--------------------------------------------------------------|
| Arduino Nano           | Brain of the system – reads sensors and controls the motor   |
| DHT11 Sensor           | Measures temperature and humidity                            |
| Soil Moisture Sensor   | Measures soil moisture level (analog input)                  |
| LCD (16x2)             | Displays current sensor readings                             |
| Relay Module           | Switches the motor ON/OFF                                    |
| 6V/12V Water Pump      | Pumps water to plants                                        |
| Buzzer + LED Indicators| Alerts and visual cues for pump activity                     |
| Jumper Wires + Breadboard | For electrical connections                              |

---

## 🧠 Software Stack

- **Arduino IDE** – to write and upload microcontroller logic
- **Python + Streamlit** – for dashboard and control interface
- **VS Code** – IDE for code development
- **Plotly** – for rich interactive graphs
- **PySerial** – to enable serial communication between Arduino and Python

---

## 🔌 Arduino Functionality

- Reads:
  - 🌡️ Temperature & 💧 Humidity using **DHT11**
  - 🌱 Soil Moisture using **YL-69** sensor
- Logic:
  - **AUTO mode**: Turns pump ON when moisture < 30%
  - **Manual mode**: Pump ON/OFF controlled through dashboard buttons
- Communicates:
  - Sends sensor data via serial port to Python
  - Displays data on LCD in two screens (Temp/Humidity and Moisture)
- Responds to commands: `ON`, `OFF`, `AUTO` via serial

---

## 🖥️ Streamlit Dashboard Features

- **📥 Read Sensor Data**: Fetch and log real-time values
- **🔛 Turn Motor ON/OFF**: Manual irrigation control
- **🌀 Switch to AUTO Mode**: Automates watering via moisture threshold
- **📈 Sensor Trends Graph**: Live plot of temperature, humidity, and moisture
- **🗂️ Data Logging**: Logged into `plant_data_log.csv` for tracking

> ⚠️ Make sure to update your COM port in the Python script:
```python
PORT = "COM5"  # Change this to your actual COM port
