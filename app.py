import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

st.set_page_config(
    page_title="EcoSense Monitor",
    page_icon="🌱",
    layout="wide"
)

# Demo values only: no physical sensors are connected.
st.title("🌱 EcoSense Monitor")
st.subheader("Smart Environmental Monitoring System")
st.info("Demo mode: the values shown below are sample data, not live measurements from real sensors.")

# Stable sample data for the dashboard
temperature = 28.4
humidity = 64
air_quality = 42
status = "Good" if air_quality <= 50 else "Moderate" if air_quality <= 100 else "Poor"

c1, c2, c3, c4 = st.columns(4)
c1.metric("🌡️ Temperature", f"{temperature} °C", "Sample value")
c2.metric("💧 Humidity", f"{humidity} %", "Sample value")
c3.metric("🌬️ Air Quality Index", air_quality, "Sample AQI")
c4.metric("🌿 Environment Status", status, "Demo status")

st.divider()
st.header("📊 Sample Environmental Trends")

now = datetime.now()
times = [now - timedelta(hours=6-i) for i in range(7)]
random.seed(7)
data = pd.DataFrame({
    "Time": times,
    "Temperature (°C)": [round(26 + random.random() * 4, 1) for _ in times],
    "Humidity (%)": [round(55 + random.random() * 20) for _ in times],
    "Air Quality Index": [round(25 + random.random() * 35) for _ in times],
}).set_index("Time")

st.line_chart(data[["Temperature (°C)", "Humidity (%)"]])
st.line_chart(data[["Air Quality Index"]])

st.header("🚨 Alerts and Recommendations")
if air_quality > 100:
    st.error("Air quality is poor in this sample. Consider improving ventilation.")
elif air_quality > 50:
    st.warning("Air quality is moderate in this sample. Monitor it regularly.")
else:
    st.success("Sample air quality is good. No demo alert is active.")

st.markdown("""
### About this project
This prototype demonstrates how an environmental monitoring dashboard can present temperature,
humidity, and air-quality readings. To measure real conditions, connect suitable sensors and a
microcontroller (for example, ESP32) and update the app to receive their readings.
""")

st.caption("Student project prototype • Built with Python and Streamlit")
