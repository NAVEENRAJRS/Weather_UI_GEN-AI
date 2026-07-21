import streamlit as st
from weather import get_weather

st.set_page_config(
    page_title="Weather Forecast",
    page_icon="🌤",
    layout="centered"
)

st.title("🌤 Weather Forecast App")

city = st.text_input("Enter City")

if st.button("Search"):

    if city == "":
        st.warning("Please enter a city name.")

    else:

        weather = get_weather(city)

        if weather:

            st.success(f"Weather in {weather['name']}")

            st.write(f"🌡 Temperature: {weather['main']['temp']} °C")

            st.write(f"🤒 Feels Like: {weather['main']['feels_like']} °C")

            st.write(f"💧 Humidity: {weather['main']['humidity']} %")

            st.write(f"🌬 Wind Speed: {weather['wind']['speed']} m/s")

            st.write(f"☁ Condition: {weather['weather'][0]['description'].title()}")

        else:
            st.error("City not found or API error.")