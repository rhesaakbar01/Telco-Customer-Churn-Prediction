import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

with open('rf_gridcv_best.pkl', 'rb') as file_1:
  model_rf = pickle.load(file_1)

def run():
    # Buat Form
    with st.form(key='Form Parameters'):
        gender = st.selectbox('gender', ('Female', 'Male'), index=0)
        group_age = st.selectbox('group_age', ('Baby', 'Child', 'Teenagers', 'Young Adult', 'Middle Age', 'Elder'), index=0)
        ever_married = st.selectbox('ever_married', ('Yes', 'No'), index=0)
        work_type = st.selectbox('work_type', ('Private', 'Self-employed', 'children', 'Govt_job'), index=0)
        residence_type = st.selectbox('residence_type', ('Urban', 'Rural'), index=0)
        st.markdown('---')

        hypertension = st.selectbox('hypertension', (0, 1), index=0, help='0 = Tekanan Darah Normal, 1 = Tekanan Darah Tinggi')
        heart_disease = st.selectbox('heart_disease', (0, 1), index=0 , help='0 = Bebas Penyakit Jantung, 1 = Punya Penyakit Jantung')
        avg_glucose_level = st.number_input('avg_glucose_level', min_value=56, max_value=270, value=100, step=1, help='Tingkat Gula Darah')
        bmi = st.number_input('bmi', min_value=14, max_value=49, value=20, step=1,help='BMI = BB/TB^2')
        smoking_status = st.selectbox('smoking_status', ('Unknown', 'never smoked', 'formerly smoked', 'smokes'), index=0)
        st.markdown('---')

        submitted = st.form_submit_button('Predict')

    data_inf = {
    "gender": gender,
    "group_age": group_age,
    "ever_married": ever_married,
    "work_type": work_type,
    "residence_type": residence_type,
    "hypertension": hypertension,
    "heart_disease": heart_disease,
    "avg_glucose_level": avg_glucose_level,
    "bmi": bmi,
    "smoking_status": smoking_status,
    }


    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        # Predict
        y_pred_final = model_rf.predict(data_inf)
        if y_pred_final == 0:
          st.write('# Tidak Berpotensi Stroke')
        else:
          st.write('# Berpotensi Stroke')

if __name__== '__main__':
    run()