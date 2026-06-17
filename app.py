import streamlit as st
import requests


st.title("AI Predictive Maintenance System")


st.write("Enter Engine Sensor Data")


values=[]


for i in range(26):

    value=st.number_input(
        f"Feature {i+1}",
        value=0.0
    )

    values.append(value)



if st.button("Predict"):

    response=requests.post(
        "http://127.0.0.1:8000/predict",
        json={
            "values":values
        }
    )


    result=response.json()


    st.success(
        f"Remaining Life: {result['Remaining_Life']} cycles"
    )