import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))
data = pickle.load(open('data.pkl', 'rb'))

st.title('Car Price Detector')

brand = st.selectbox('Brand', data['Brand'].unique())
car_model = st.selectbox('model', data[data['Brand'] == brand]['model'].unique())
Year = st.number_input('Year', min_value=1900, max_value=2024)
km = st.number_input('Total KiloMeters Driven', step = 1)
age = 2024 - Year
# st.text_area('Age of the Car:', age)
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
owner = st.selectbox('Owner', ['second', 'first'])
fueltype = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'Hybrid/CNG', 'hybrid'])


if st.button('Predict Price'):
    # query = np.array([brand, car_model, Year, age, km, transmission, owner, fueltype]).reshape(1, 8)

    st.markdown(
    """
    <div style="
        background-color:#f193f2; 
        padding:20px; 
        border-radius:10px; 
    ">
        <h3 style="color:#000;">Your Car Configurations</h3>
        <p style="color:#2838d2;>Brand/ Company: {}</p>
        <p style="color:#2838d2;">Model: {}</p>
        <p style="color:#2838d2;">Manufactured Year: {}</p>
        <p style="color:#2838d2;">Age of Car till now (2024): {} Years</p>
        <p style="color:#2838d2;">Total Kilo Meters Driven: {} Km</p>
        <p style="color:#2838d2;">Transmission: {}</p>
        <p style="color:#2838d2;">Ownership: {}</p>
        <p style="color:#2838d2;">Fuel Type: {}</p>
    </div>
    """.format(brand, car_model, Year, age, km, transmission, owner, fueltype),
    unsafe_allow_html=True
)


    transmission = 1 if transmission == 'Manual' else 2
    owner = 1 if owner == 'second' else 2

    if fueltype == 'Petrol':
        fueltype = 1
    elif fueltype == 'Diesel':
        fueltype = 2
    elif fueltype == 'Hybrid/CNG':
        fueltype = 3
    else:
        fueltype = 4

    
    predicted_price = model.predict(np.array([brand, car_model, age, km, transmission, owner, fueltype]).reshape(1, 7))
    st.success(f'The Predicted Price of the Car is: ₹{int(predicted_price)}')