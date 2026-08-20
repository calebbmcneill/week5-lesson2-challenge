import requests
import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd

# Load your API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    """
    Fetch weather for the given city and print it nicely.
    """
    # 1. Create the API endpoint URL
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # 2. Set query parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # temperature in Celsius
    }
    
    # 3. Make the request
    response = requests.get(url, params=params)
    
    # 4. Parse JSON
    data = response.json()
    
    # 5. Extract key info
    city_name = data["name"]
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    low = data["main"]["temp_min"]
    high = data["main"]["temp_max"]
    wind_speed = data["wind"]["speed"]
    wind_deg = data["wind"]["deg"]

    df = pd.DataFrame({
        "Label": ["Low", "Average", "High"],
        "Temperature": [{low}, {temp}, {high}]
    })
    

    # 1. Title and description
    st.title("My City Weather")
    st.write("The weather in any US city, anytime.")
    
    # 6. Print
    st.write(f"In {city_name}, it is {temp}°C with {description} and {humidity}% humidity.")
    col1 , col2 = st.columns(2)

    with col1:
        if temp >= 25:
            st.write("Whoa! That's Hot!")
        elif temp <= 10:
            st.write("Chilly!")
        else:
            st.write("Just right for this time of year.")

    with col2:
        st.title("Detailed Statistics")
        st.dataframe(df)
        st.write("Wind Speed: ", {wind_speed}, "Wind Direction in Degrees: ", {wind_deg})

city = st.text_input("For what city in the US would you like to know the weather? ")
get_weather(city)