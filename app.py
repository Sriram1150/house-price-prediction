import streamlit as st
import pandas as pd
import joblib
import boto3
import os

bucket_name = "house-price-mlops-models"

model_file = "house_price_model.pkl"

s3 = boto3.client("s3")

if not os.path.exists(model_file):

    s3.download_file(
        bucket_name,
        model_file,
        model_file
    )

model = joblib.load(model_file)

st.set_page_config(page_title="House Price Prediction")

st.title("House Price Prediction App")

st.write("Enter House Details")

# Numerical Inputs
area = st.number_input("Area", min_value=100)

bedrooms = st.number_input("Bedrooms", min_value=1)

bathrooms = st.number_input("Bathrooms", min_value=1)

stories = st.number_input("Stories", min_value=1)

parking = st.number_input("Parking", min_value=0)

# Categorical Inputs
mainroad = st.selectbox("Main Road", ["yes", "no"])

guestroom = st.selectbox("Guest Room", ["yes", "no"])

basement = st.selectbox("Basement", ["yes", "no"])

hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])

airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])

prefarea = st.selectbox("Preferred Area", ["yes", "no"])

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["furnished", "semi-furnished", "unfurnished"]
)

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "mainroad": [mainroad],
        "guestroom": [guestroom],
        "basement": [basement],
        "hotwaterheating": [hotwaterheating],
        "airconditioning": [airconditioning],
        "parking": [parking],
        "prefarea": [prefarea],
        "furnishingstatus": [furnishingstatus]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")