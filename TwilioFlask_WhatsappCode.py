import requests
from twilio.rest import Client

# ThingSpeak Details
THINGSPEAK_CHANNEL_ID = "2855155"  # Replace with your channel ID
THINGSPEAK_API_KEY = "UEFBE2B2QFY7K9H9"  # Replace with your API key
THINGSPEAK_URL = f"https://api.thingspeak.com/channels/{THINGSPEAK_CHANNEL_ID}/feeds.json?api_key={THINGSPEAK_API_KEY}&results=1"

# Twilio Credentials
TWILIO_SID = "ACa38c1e8d1d89533161485faa9fc671fe"  # Replace with your Twilio SID
TWILIO_AUTH_TOKEN = "9c374abdca71c0c266ec8b4b46ec08ca"  # Replace with your Twilio Auth Token
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio Sandbox WhatsApp Number
OWNER_WHATSAPP_NUMBER = "whatsapp:+919632022024"  # Replace with the owner's WhatsApp number

# Thresholds
MOISTURE_THRESHOLD = 2600
TEMP_THRESHOLD = 40
HUMIDITY_THRESHOLD = 80
RAIN_THRESHOLD = 2000

def get_thingspeak_data():
    """Fetch the latest data from ThingSpeak."""
    try:
        response = requests.get(THINGSPEAK_URL, timeout=10)  # Added timeout
        response.raise_for_status()  # Raise error if request fails
        feeds = response.json().get("feeds", [])

        if feeds:
            latest_entry = feeds[-1]  # Get the latest data
            
            # Parse sensor values safely
            soil_moisture = int(latest_entry.get("field1", 0) or 0)
            temperature = float(latest_entry.get("field2", 0) or 0)
            humidity = float(latest_entry.get("field3", 0) or 0)
            rain = int(latest_entry.get("field4", 0) or 0)

            print(f"Debug - Moisture: {soil_moisture}, Temp: {temperature}, Humidity: {humidity}, Rain: {rain}")
            return soil_moisture, temperature, humidity, rain
    except requests.RequestException as e:
        print(f"Error fetching ThingSpeak data: {e}")

    return None  # Return None if data fetch fails

def send_whatsapp_alert(message):
    """Send WhatsApp alert via Twilio."""
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    try:
        msg = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            to=OWNER_WHATSAPP_NUMBER,
            body=message
        )
        print("WhatsApp message sent successfully! Message SID:", msg.sid)
    except Exception as e:
        print(f"Failed to send WhatsApp message: {e}")

def main():
    data = get_thingspeak_data()
    if data:
        soil_moisture, temperature, humidity, rain = data

        # Always include sensor readings
        alert_message = (
            "🌱 Smart Irrigation System Update 🌱\n"
            f"💧 Soil Moisture: {soil_moisture}\n"
            f"🌡️ Temperature: {temperature}°C\n"
            f"💦 Humidity: {humidity}%\n"
            f"☔ Rain Level: {rain}\n\n"
        )

        # Append alerts based on thresholds
        alerts = []
        if soil_moisture > MOISTURE_THRESHOLD:
            alerts.append(f"🚨 Soil is DRY! Moisture Level: {soil_moisture}")
        if temperature > TEMP_THRESHOLD:
            alerts.append(f"🔥 High Temperature Alert! Temp: {temperature}°C")
        if humidity > HUMIDITY_THRESHOLD:
            alerts.append(f"💧 High Humidity Alert! Humidity: {humidity}%")
        if rain >= RAIN_THRESHOLD:
            alerts.append("🌧️ Rain detected!")

        # Add alerts if any
        if alerts:
            alert_message += "⚠️ ALERTS ⚠️\n" + "\n".join(alerts)

        send_whatsapp_alert(alert_message)
        print("Message Sent:", alert_message)
    else:
        print("Failed to fetch data from ThingSpeak.")

if __name__ == "__main__":
    main()
