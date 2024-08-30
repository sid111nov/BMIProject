import streamlit as st
from src.pipeline.CustomData import CustomData
from src.pipeline.prediction_pipeline import PredictionPipeline
import numpy as np
import os
import application as ap


gender = st.selectbox('Gender',["Male","Female"])

height = st.selectbox('Height in cm',range(120,250))

weight = st.selectbox('Weight in Kg',range(35,800))

data=CustomData(
            gender=gender,
            height=height,
            weight=weight         

        )
        
data_df = data.get_data_as_data_frame()
        


if st.button("Submit"):
    predict_pipeline=PredictionPipeline(data_df)
    bmi  = predict_pipeline.predict()
    bmi_result = ap.getBMIMapping(bmi)
    st.title(bmi_result)