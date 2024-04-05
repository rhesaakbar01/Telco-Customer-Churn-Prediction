import streamlit as st
import pickle
import json
import pandas as pd
import numpy as np

# Load Model
with open('model_adaboost_improve.pkl', 'rb') as file_1:
    model_adaboost_improve = pickle.load(file_1)

def run():
    # Buat Form
    with st.form(key='Form Parameters'):
        gender = st.selectbox('gender', ('Female', 'Male'), index=0)
        SeniorCitizen = st.selectbox('Senior Citizen', (0, 1), index=0, help='1 = Senior, 0 = Bukan Senior')
        Partner = st.selectbox('Partner', ('Yes', 'No'), index=0)
        Dependents = st.selectbox('Dependents', ('Yes', 'No'), index=0, help='Indikator apakah pelanggan memiliki tanggungan (misalnya: anak-anak) atau tidak.')
        tenure = st.number_input('Tenure',  min_value=1, max_value=72, help='Jumlah bulan yang pelanggan telah menggunakan layanan')
        PhoneService = st.selectbox('Phone Service', ('Yes', 'No'), index=0)
        MultipleLines = st.selectbox('MultipleLines', ('No phone service', 'No', 'Yes'), index=0, help='Indikator apakah pelanggan memiliki beberapa saluran telepon atau tidak')
        InternetService = st.selectbox('Internet Service', ('DSL', 'Fiber optic', 'No'), index=0 , help='Jenis layanan internet yang digunakan oleh pelanggan')
        OnlineSecurity = st.selectbox('Online Security', ('No internet service', 'Yes', 'No'), index=0, help='Indikator apakah pelanggan memiliki fitur keamanan online atau tidak')
        OnlineBackup = st.selectbox('Online Backup', ('Yes', 'No', 'No internet service'), index=0, help='Indikator apakah pelanggan memiliki fitur backup online atau tidak')
        DeviceProtection = st.selectbox('Device Protection', ('No', 'Yes', 'No internet service'), index=0, help='Jumlah biaya bulanan yang dibebankan kepada pelanggan')
        TechSupport = st.selectbox('Tech Support', ('No', 'Yes', 'No internet service'), help='Indikator apakah pelanggan memiliki dukungan teknis atau tidak', index=0)
        StreamingTV = st.selectbox('Streaming TV', ('No', 'Yes', 'No internet service'), help= 'Indikator apakah pelanggan memiliki layanan streaming TV atau tidak',index=0)
        StreamingMovies = st.selectbox('Streaming Movies', ('No', 'Yes', 'No internet service'), help='Indikator apakah pelanggan memiliki layanan streaming film atau tidak', index=0)
        Contract = st.selectbox('Contract', ('Month-to-month', 'One year', 'Two year'),help='Tipe kontrak yang dimiliki oleh pelanggan', index=0)
        PaperlessBilling = st.selectbox('PaperlessBilling', ('Yes', 'No'), help= 'Indikator apakah pelanggan menerima tagihan secara elektronik atau kertas',index=0)
        PaymentMethod = st.selectbox('Payment Method', ('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'), index=0)
        MonthlyCharges = st.number_input('Monthly Charges', min_value=19, max_value=118, help='Jumlah biaya bulanan yang dibebankan kepada pelanggan')
        TotalCharges = st.number_input('Total Charges', min_value=19, max_value=8680, help='Total biaya yang dibebankan kepada pelanggan')
        st.markdown('---')

        submitted = st.form_submit_button('Predict')

    data_inf = {
    "gender": gender,
    "SeniorCitizen": SeniorCitizen,
    "Partner": Partner,
    "Dependents": Dependents,
    "tenure": tenure,
    "PhoneService": PhoneService,
    "MultipleLines": MultipleLines,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection": DeviceProtection,
    "TechSupport": TechSupport,
    "StreamingTV": StreamingTV,
    "Streaming Movies": StreamingMovies,
    "Contract": Contract,
    "PaperlessBilling": PaperlessBilling,
    "PaymentMethod": PaymentMethod,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges,
    }


    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        # Predict
        y_pred_final = model_adaboost_improve.predict(data_inf)
        if y_pred_final == 1:
          st.write('# Berpotensi Churn')
        else:
          st.write('# Berpotensi tidak Churn')

if __name__== '__main__':
    run()