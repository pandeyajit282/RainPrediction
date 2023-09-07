import streamlit as st
import pandas as pd
import numpy as np
import datetime
import joblib
import requests
from PIL import Image


# Load the model
model = joblib.load("./models/bagging.pkl")

def predict_rainfall():
    # DATE
    date = st.date_input("Date")
    day = float(date.day)
    month = float(date.month)
    # MinTemp
    minTemp = st.number_input("Min Temperature")
    # MaxTemp
    maxTemp = st.number_input("Max Temperature")
    # Rainfall
    rainfall = st.number_input("Rainfall")
    # Evaporation
    evaporation = st.number_input("Evaporation")
    # Sunshine
    sunshine = st.number_input("Sunshine")
    # Wind Gust Speed
    windGustSpeed = st.number_input("Wind Gust Speed")
    # Wind Speed 9am
    windSpeed9am = st.number_input("Wind Speed 9am")
    # Wind Speed 3pm
    windSpeed3pm = st.number_input("Wind Speed 3pm")
    # Humidity 9am
    humidity9am = st.number_input("Humidity 9am")
    # Humidity 3pm
    humidity3pm = st.number_input("Humidity 3pm")
    # Pressure 9am
    pressure9am = st.number_input("Pressure 9am")
    # Pressure 3pm
    pressure3pm = st.number_input("Pressure 3pm")
    # Temperature 9am
    temp9am = st.number_input("Temperature 9am")
    # Temperature 3pm
    temp3pm = st.number_input("Temperature 3pm")
    # Cloud 9am
    cloud9am = st.number_input("Cloud 9am")
    # Cloud 3pm
    cloud3pm = st.number_input("Cloud 3pm")
    # Cloud 3pm
    location = st.number_input("Location")
    # Wind Dir 9am
    winddDir9am = st.number_input("Wind Dir 9am")
    # Wind Dir 3pm
    winddDir3pm = st.number_input("Wind Dir 3pm")
    # Wind Gust Dir
    windGustDir = st.number_input("Wind Gust Dir")
    # Rain Today
    rainToday = st.selectbox("Rain Today", ["No", "Yes"])

    rainToday_value = 0 if rainToday == "No" else 1

    input_lst = [location , minTemp , maxTemp , rainfall , evaporation , sunshine ,
                 windGustDir , windGustSpeed , winddDir9am , winddDir3pm , windSpeed9am , windSpeed3pm ,
                 humidity9am , humidity3pm , pressure9am , pressure3pm , cloud9am , cloud3pm , temp9am , temp3pm ,
                 rainToday_value , month , day]

    input_df = pd.DataFrame([input_lst], columns=['Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation',
                                                  'Sunshine', 'WindGustDir', 'WindGustSpeed', 'WindDir9am',
                                                  'WindDir3pm', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am',
                                                  'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm',
                                                  'Temp9am', 'Temp3pm', 'RainToday', 'Month', 'Day'])
    pred = model.predict(input_df)
    output = pred[0]
    if output == 0:
        image1 = Image.open("./sunny.png")
        st.image(image1)
        st.write("It will be sunny!")
    else:
        image2 = Image.open("./rainy.png")
        st.image(image2)
        st.write("It will be rainy!")

def main():
    # Set a title for your app
    st.title('Rainfall Prediction App')
    st.write('Enter input data:')
    predict_rainfall()


if __name__ == "__main__":
    main()
