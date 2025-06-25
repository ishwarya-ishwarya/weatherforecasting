import streamlit as st
import requests

# --- Replace with your OpenWeatherMap API Key ---
API_KEY = "3248cb868337deeed87670a8bff6ce84"
# ------------------------------------------------

st.set_page_config(page_title="Weather Forecast", page_icon="🌦️")

st.title("🌦️ Weather Forecast App")
st.markdown("Enter a city name below to get the current weather forecast.")

city = st.text_input("City Name", "")

if st.button("Get Weather") and city:
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get('cod') == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }

            st.subheader(f"Weather in {weather_data['city']}")
            st.image(f"http://openweathermap.org/img/wn/{weather_data['icon']}@2x.png")
            st.write(f"**🌡️ Temperature:** {weather_data['temperature']} °C")
            st.write(f"**☁️ Condition:** {weather_data['description'].title()}")
            st.write(f"**💧 Humidity:** {weather_data['humidity']}%")
            st.write(f"**🌬️ Wind Speed:** {weather_data['wind_speed']} m/s")

        else:
            st.error(data.get('message', 'City not found or API error.'))

    except requests.exceptions.RequestException as e:
        st.error(f"🌐 Network error: {e}")
    except KeyError:
        st.error("Invalid API response. Please check your API key or city name.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

elif city == "":
    st.info("🔍 Please enter a city name to get the weather.")
