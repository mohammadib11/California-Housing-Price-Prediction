from controller.LoadModel import LoadModel
from controller.GetPrediction import GetPrediction
import streamlit as st

st.title('California House Price Prediction')
st.write('Enter the required values to predict the house price')

longitude = st.number_input('Longitude value (-123,117)' , min_value=-123.080000, max_value=117.260000, step=0.01)
latitude = st.number_input('Latitude value (32,38)' , min_value=32.750000, max_value=38.470000, step=0.01)
median_age = st.number_input('Median age value (2,40)' , min_value=2.0, max_value=40.0, step=0.1)
total_rooms = st.number_input('Total rooms value (18,3480)' , min_value=18.0, max_value=3480.0, step=0.1)
total_bedrooms = st.number_input('Total bedrooms value (3,717)' , min_value=3.0, max_value=717.0, step=0.1)
population = st.number_input('Population value (8,1909)' , min_value=8.0, max_value=1909.0, step=0.1)
households = st.number_input('Households value (8,668)' , min_value=8.0, max_value=668.0, step=0.1)
median_income = st.number_input('Median income value (0.7,5)' , min_value=0.7160, max_value=5.17950, step=0.0001)
ocean_proximity = st.number_input('Ocean proximity value (0,4)' , min_value=0.0, max_value=4.0, step=1.0)

model = LoadModel('model/California_House_Price.pkl')

if st.button('Start prediction') :
    prediction = GetPrediction(model, [longitude,latitude,median_age,total_rooms,total_bedrooms,population,households,median_income,ocean_proximity])
    st.write('The house price prediction is {:0,.2f}'.format(float(prediction)), '$')

