import streamlit as st
import serial
import pandas as pd
import plotly.express as px
from datetime import datetime

# Set Streamlit config (must be first command)
st.set_page_config(page_title="Smart Plant Dashboard", layout="wide")

# === Setup Arduino details ===
PORT = "COM5"  # ✅ Replace with your actual port
BAUD_RATE = 9600

st.title("🌿 Smart Plant Health Dashboard")

# === Initialize session data ===
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Timestamp", "Temperature", "Humidity", "Moisture"])

# === Layout buttons for motor control and sensor reading ===
col1, col2, col3, col4 = st.columns(4)

# Read Sensor Button
if col1.button("📥 Read Sensor Data"):
    try:
        arduino = serial.Serial(PORT, BAUD_RATE, timeout=2)
        line = arduino.readline().decode("utf-8").strip()
        arduino.close()

        if line and "Temperature" in line:
            parts = line.split(",")
            temp = float(parts[0].split(":")[1])
            hum = float(parts[1].split(":")[1])
            moisture = float(parts[2].split(":")[1])
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Save to session
            new_data = {"Timestamp": timestamp, "Temperature": temp, "Humidity": hum, "Moisture": moisture}
            st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([new_data])], ignore_index=True)
            st.session_state.data.to_csv("plant_data_log.csv", index=False)

            # Display metrics
            mcol1, mcol2, mcol3 = st.columns(3)
            mcol1.metric("🌡️ Temperature", f"{temp:.2f} °C")
            mcol2.metric("💧 Humidity", f"{hum:.2f} %")
            mcol3.metric("🌱 Moisture", f"{moisture:.2f} %")

        else:
            st.warning("⚠️ No sensor data received. Try again.")

    except serial.SerialException:
        st.error(f"❌ Could not connect to Arduino on port {PORT}. Is it connected and not in use?")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# === Motor Control Buttons ===
def send_command(command: str):
    try:
        arduino = serial.Serial(PORT, BAUD_RATE, timeout=2)
        arduino.write((command + "\n").encode())
        arduino.close()
        st.success(f"✅ Command sent: {command}")
    except Exception as e:
        st.error(f"❌ Failed to send '{command}': {e}")

if col2.button("🔛 Turn Motor ON"):
    send_command("ON")

if col3.button("🔴 Turn Motor OFF"):
    send_command("OFF")

if col4.button("🌀 Switch to AUTO Mode"):
    send_command("AUTO")

# === Live Chart Section ===
st.markdown("---")
st.subheader("📈 Sensor Trends")

if not st.session_state.data.empty:
    chart_data = st.session_state.data.tail(30)
    fig = px.line(
        chart_data,
        x="Timestamp",
        y=["Temperature", "Humidity", "Moisture"],
        labels={"value": "Sensor Value", "variable": "Sensor"},
        title="Recent Sensor Readings"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("👉 Click 'Read Sensor Data' to load data from Arduino.")
