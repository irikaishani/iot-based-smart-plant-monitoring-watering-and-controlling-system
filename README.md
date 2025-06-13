# 🌿 Smart Plant Health Monitoring and Watering System

An **IoT-based Precision Agriculture Project** that automates plant watering by monitoring **real-time soil moisture, temperature, and humidity**, while offering both **manual and automatic motor control** through a user-friendly **Streamlit dashboard**.

---
![Dashboard Screenshot](https://private-user-images.githubusercontent.com/177468201/455006630-2fc61cbf-de82-488d-bf5f-c95775344f00.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDk4NDA1MzcsIm5iZiI6MTc0OTg0MDIzNywicGF0aCI6Ii8xNzc0NjgyMDEvNDU1MDA2NjMwLTJmYzYxY2JmLWRlODItNDg4ZC1iZjVmLWM5NTc3NTM0NGYwMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYxM1QxODQzNTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03ZTY2N2Q0M2QxMzNlM2ZhOTUxNDE4MGI5MzgyYzY3NTZjZjZhZmY4ZGZiY2QxMTliZjczNmJkYjQ4ZDk0MzVmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.4NaNwQefJSKHe8_mlMdDA98Zr-kT8lVD6KpsRjAPo4w)
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

---

## 🚀 How to Run the Project

### 1. Hardware Setup
- Connect all components (DHT11, soil moisture sensor, relay module, LCD, LEDs, pump, buzzer) to the Arduino Nano as per the circuit diagram.
- Plug the Arduino Nano into your computer using a USB cable.

---

### 2. Find the COM Port using Arduino IDE

#### 🧩 Step 1: Install Arduino IDE
Download and install the latest Arduino IDE from:  
👉 https://www.arduino.cc/en/software

#### 🔌 Step 2: Check Connected Port
- Open Arduino IDE.
- Go to `Tools > Board > Arduino Nano` (optional, for clarity).
- Go to `Tools > Port` — note the **COM port** listed (e.g., `COM3`, `COM5`, etc.).

You do **not** need to paste or upload any code in the Arduino IDE — it’s just used here to find the correct port.

---

### 3. Software Setup

#### Install the required Python packages:
```bash
pip install streamlit pandas plotly pyserial

```

### 4.Make sure to update your COM port in the Python script:
```bash
PORT = "COM5"  # Change this to your actual COM port

```

### 5. Launch the streamlit dashboard:
```bash
streamlit run app.py

```

---

## 📍 Conclusion

This project demonstrates a complete **IoT-based smart plant watering system** that integrates sensor monitoring, automated irrigation control, and real-time data visualization. It helps:

- Save water by only irrigating when needed.
- Reduce manual monitoring by automating decisions.
- Visualize temperature, humidity, and soil moisture trends interactively.
- Provide a scalable framework for smart farming.

A step forward in building **smart, sustainable, and efficient agriculture** solutions with minimal resources and open-source tools. 🌾💧🌍








