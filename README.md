# ESP32 Smart Irrigation System

## Overview
This project is a smart irrigation system using an ESP32, which collects environmental data such as soil moisture, temperature, humidity, and rain detection. It communicates this data via MQTT and ThingSpeak and controls a water pump based on soil moisture and rain conditions.

## Features
- Reads sensor values (soil moisture, temperature, humidity, and rain detection)
- Publishes sensor data to an MQTT broker
- Sends data to ThingSpeak for remote monitoring
- Controls a water pump based on soil moisture and rain conditions
- Provides LED indicators for temperature and humidity levels

## Hardware Requirements
- ESP32 development board
- DHT11 sensor (Temperature & Humidity)
- Soil moisture sensor
- Rain sensor (Analog)
- Relay module for pump control
- LEDs for temperature and humidity indication
- Power supply (5V or 3.3V as required by sensors)

## Software Requirements
- Arduino IDE with ESP32 board support
- Required Libraries:
  - `WiFi.h` (Built-in for ESP32)
  - `PubSubClient.h` (For MQTT communication)
  - `HTTPClient.h` (For sending data to ThingSpeak)
  - `DHT.h` (For temperature and humidity sensing)

## Setup

1. **Install Libraries**
   - Open Arduino IDE and install the required libraries from the Library Manager.

2. **Update Configuration**
   - Set your WiFi SSID and password in the following lines:
     ```cpp
     const char* ssid = "Your_WiFi_SSID";
     const char* password = "Your_WiFi_Password";
     ```
   - Update the MQTT broker IP address and port:
     ```cpp
     const char* mqtt_server = "Your_MQTT_Broker_IP";
     const int mqtt_port = 1883;
     ```
   - Replace the ThingSpeak API key with your own:
     ```cpp
     const char* thingSpeakApiKey = "Your_ThingSpeak_API_Key";
     ```

3. **Wiring Connections**
   - **DHT11 Sensor:** Data pin to GPIO14
   - **Soil Moisture Sensor:** Analog output to GPIO33
   - **Rain Sensor:** Analog output to GPIO34
   - **Relay Module:** IN pin to GPIO27 (Pump Control)
   - **Temperature LED:** GPIO35
   - **Humidity LED:** GPIO32

4. **Upload the Code**
   - Connect the ESP32 to your computer via USB.
   - Select the correct board and port in Arduino IDE.
   - Click the upload button.

5. **Run and Monitor**
   - Open the Serial Monitor (115200 baud rate) to see sensor readings and MQTT/ThingSpeak status.
   - Ensure the MQTT broker is running and subscribed to the relevant topics.

## MQTT Topics
- `irrigation/soilMoisture`: Publishes soil moisture values
- `irrigation/temperature`: Publishes temperature values
- `irrigation/humidity`: Publishes humidity values
- `irrigation/rain`: Publishes rain detection status (`1` for rain, `0` for no rain)
- `irrigation/pumpControl`: Publishes `ON` or `OFF` based on pump status

## ThingSpeak Integration
- Data is sent to ThingSpeak every 5 seconds.
- Fields mapping:
  - Field 1: Soil Moisture
  - Field 2: Temperature
  - Field 3: Humidity
  - Field 4: Rain Status

## Troubleshooting
- **WiFi Not Connecting?**
  - Ensure WiFi credentials are correct.
  - Check router settings for device limits.
- **MQTT Connection Fails?**
  - Verify MQTT broker IP address and ensure it’s running.
  - Check network firewall settings.
- **No Sensor Data?**
  - Ensure all sensors are properly connected.
  - Verify power supply voltage levels.
- **Pump Not Activating?**
  - Check soil moisture sensor readings.
  - Verify relay module wiring.

## Future Improvements
- Integrate a database (SQLite/Firebase) to store historical sensor data.
- Add a mobile app for remote monitoring and manual pump control.
- Implement AI-based irrigation scheduling for optimized water usage.

## Contributing
Contributions are welcome! Feel free to fork this repository, make modifications, and submit a pull request.

## License
This project is open-source. Feel free to modify and use it for your own applications.

