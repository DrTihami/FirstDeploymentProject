import warnings
import streamlit as st
import pandas as pd
import pickle

warnings.filterwarnings('ignore')
# Load the model
with open('model1.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
# Load the Scaler
with open('scaler1.pkl', 'rb') as file:
    loaded_scaler = pickle.load(file)
# Headings and creator name
st.header('Insurance Premium Prediction App')
st.write('Created by: Dr Shabir Ahmad')

st.write('Enter the details to know your Insurance Premium')

# Input fields
Age = st.slider("Select your age", 18, 65)
col1, col2, col3 = st.columns(3)
with col1:
    Diabetes = st.selectbox("Are you Diabetic?", ("Yes", "No"))
with col2:
    BloodPressureProblems = st.selectbox("High Blood Pressure?", ("Yes", "No"))
with col3:
    AnyTransplants = st.selectbox("If you had a Transplant?", ("Yes", "No"))
col4, col5 = st.columns(2)
with col4:
    AnyChronicDiseases = st.selectbox("Any chronic diseases?", ("Yes", "No"))
with col5:
    Height = st.slider("Select your Height in CM", 145, 188)
Weight = st.slider("Select your Weight in KG", 51, 132)
col6, col7, col8 = st.columns(3)
with col6:
    KnownAllergies = st.selectbox("Are you Allergic?", ("Yes", "No"))
with col7:
    HistoryOfCancerInFamily = st.selectbox("History of Family Cancer?", ("Yes", "No"))
with col8:
    NumberOfMajorSurgeries = st.selectbox("No of surgeries undergone till date?", [0, 1, 2, 3])

# Map Yes/No to 1/0
Diabetes = 1 if Diabetes == 'Yes' else 0
BloodPressureProblems = 1 if BloodPressureProblems == 'Yes' else 0
AnyTransplants = 1 if AnyTransplants == 'Yes' else 0
AnyChronicDiseases = 1 if AnyChronicDiseases == 'Yes' else 0
KnownAllergies = 1 if KnownAllergies == 'Yes' else 0
HistoryOfCancerInFamily = 1 if HistoryOfCancerInFamily == 'Yes' else 0

# Prepare the input data for prediction
input_data = {
        'Age': [Age],
        'Diabetes': [Diabetes],
        'BloodPressureProblems': [BloodPressureProblems],
        'AnyTransplants': [AnyTransplants],
        'AnyChronicDiseases': [AnyChronicDiseases],
        'Height': [Height],
        'Weight': [Weight],
        'KnownAllergies': [KnownAllergies],
        'HistoryOfCancerInFamily': [HistoryOfCancerInFamily],
        'NumberOfMajorSurgeries': [NumberOfMajorSurgeries]
}

# Convert input data to dataframe
input_df = pd.DataFrame(input_data)

# scale the input data
scaled_df = loaded_scaler.transform(input_df)

# Make prediction
if st.button('Predict Premium Price'):
    predicted_price = loaded_model.predict(scaled_df)
    st.write(f'The predicted premium price is Rupees : {predicted_price[0]:.2f}')