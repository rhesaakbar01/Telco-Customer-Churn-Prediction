import pandas as pd
import streamlit as st
import eda
import prediction
from PIL import Image
page = st.sidebar.selectbox('Choose Page:', ('Landing Page','Data Explorasi','Data Prediksi'))

if page == 'Landing Page':
    st.title('Milestone 2')
    st.write('')
    st.image('customer_churn.jpg')
    st.write('')
    st.write('Name : Rhesa Akbar Elvarettano')
    st.write('Batch : SBY-003')
    st.write('Objective: Membuat model Classification dengan memprediksi perilaku customers untuk mengetahui apakah pelanggan melakukan churn atau tidak dengan menggunakan dataset.')
    st.write('')
    st.write('Please select menu on the left bar !')
    st.write('')
elif page == 'Data Explorasi':
    eda.run()
else:
    prediction.run()