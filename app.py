import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("house_price_model.pkl")

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