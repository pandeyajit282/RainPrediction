import streamlit as st
import pandas as pd
import numpy as np
import datetime
import joblib
import requests
from PIL import Image
import sklearn
from sklearn.ensemble import BaggingClassifier

st.set_page_config(
    page_title="Rainfall Prediction App",
    page_icon=":partly_sunny:",  # You can use any emoji as an icon
    layout="wide",  # Use "wide" layout for two sections side by side
    initial_sidebar_state="collapsed",  # Sidebar initially collapsed
    theme="light",  # Choose the light theme
)

st.markdown(
    """
    <style>
        .css-1v3fvcr {  /* Primary color */
            color: #F63366;
        }
        body {  /* Background color */
            background-color: #FFFFFF;
        }
        .css-3r66q9 {  /* Secondary background color */
            background-color: #F0F2F6;
        }
        .css-1aumxhk {  /* Text color */
            color: #262730;
        }
        .stApp {  /* Font */
            font-family: "sans serif";
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load the model
model = joblib.load("./models/bagging.pkl")

def predict_rainfall():
    col1, col2 = st.columns(2)  # Create two columns

    with col1:
        # DATE
        date = st.date_input("Date")
        day = float(date.day)
        month = float(date.month)
        # MinTemp
        minTemp = st.number_input("Min Temperature",value = 30 )
        # MaxTemp
        maxTemp = st.number_input("Max Temperature", value= 13.4)
        # Rainfall
        rainfall = st.number_input("Rainfall", value = 0.6)
        # Evaporation
        evaporation = st.number_input("Evaporation", value = 2.4)
        # Sunshine
        sunshine = st.number_input("Sunshine", value = 8.3)
        # Wind Gust Speed
        windGustSpeed = st.number_input("Wind Gust Speed", value = 44)
        # Wind Speed 9am
        windSpeed9am = st.number_input("Wind Speed 9am", value = 20)
        # Wind Speed 3pm
        windSpeed3pm = st.number_input("Wind Speed 3pm", value =  24)
        # Humidity 9am
        humidity9am = st.number_input("Humidity 9am", value =71)
        # Humidity 3pm
        humidity3pm = st.number_input("Humidity 3pm", value =22)
    with col2:
        # Pressure 9am
        pressure9am = st.number_input("Pressure 9am", value = 1007.7)
        # Pressure 3pm
        pressure3pm = st.number_input("Pressure 3pm", value = 1007.1)
        # Temperature 9am
        temp9am = st.number_input("Temperature 9am", value =  16.9)
        # Temperature 3pm
        temp3pm = st.number_input("Temperature 3pm", value =21.8)
        # Cloud 9am
        cloud9am = st.number_input("Cloud 9am",value = 8)
        # Cloud 3pm
        cloud3pm = st.number_input("Cloud 3pm", value = 0)
        # Cloud 3pm
        location = st.number_input("Location", value = 30)
        # Wind Dir 9am
        winddDir9am = st.number_input("Wind Dir 9am", value = 5)
        # Wind Dir 3pm
        winddDir3pm = st.number_input("Wind Dir 3pm", value = 3)
        # Wind Gust Dir
        windGustDir = st.number_input("Wind Gust Dir", value = 4)
        # Rain Today
        rainToday = st.selectbox("Rain Today", ["No", "Yes"])

    rainToday_value = 0 if rainToday == "No" else 1

    if st.button("Predict"):
        # When the button is clicked, perform the prediction
        input_lst = [location, minTemp, maxTemp, rainfall, evaporation, sunshine,
                     windGustDir, windGustSpeed, winddDir9am, winddDir3pm, windSpeed9am, windSpeed3pm,
                     humidity9am, humidity3pm, pressure9am, pressure3pm, cloud9am, cloud3pm, temp9am, temp3pm,
                     rainToday_value, month, day]

        input_df = pd.DataFrame([input_lst], columns=['Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation',
                                                      'Sunshine', 'WindGustDir', 'WindGustSpeed', 'WindDir9am',
                                                      'WindDir3pm', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am',
                                                      'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm',
                                                      'Temp9am', 'Temp3pm', 'RainToday', 'Month', 'Day'])
        
        pred = model.predict(input_df)
        output = pred[0]
        if output == 0:
            image1 = Image.open("./images/sunny.png")
            st.image(image1)
            st.header("It will be sunny!")
        else:
            image2 = Image.open("./images/rainy.png")
            st.image(image2)
            st.header("It will be rainy!")

    
def main():
    # Set a title for your app
    st.title('Rainfall Prediction App')
    st.write('Enter input data:')
    predict_rainfall()


if __name__ == "__main__":
    main()
