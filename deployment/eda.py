import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    # Membuat Tittle
    st.title('Prediksi Churn customers')

    # Membuat Sub Header
    st.subheader('Eda untuk Analisa Dataset Telco Customer Churn')

    # Menambahakan Gambar
    st.image('customer_churn.jpg', caption= 'customer_churn')

    # Menambahkan Deskripsi
    st.write('## WELCOME')
    st.write('Pada page kali ini, penulis akan melakukan ekspolrasi sederhana pada dataset Telco Customer Churn dengan visualisasi sederhana.')

    # Membuat Garis Lurus
    st.markdown('---')

    df = pd.read_csv('p1m2_Telco-Customer-Churn.csv')
    st.dataframe(df)

    # Membuat Garis Lurus
    st.markdown('---')

    # Membuat Countplot
    st.write('### Menampilkan kolom target No Churn & Churn')
    fig = plt.figure(figsize=(6,6))
    ax = sns.countplot(data=df, x='Churn', palette='mako')
    plt.bar_label(plt.gca().containers[0])
    plt.bar_label(plt.gca().containers[1])
    plt.xticks([0,1], ['No', 'Yes'])
    st.pyplot(fig)
    st.write('Dari informasi visualisasi kolom target diatas, diketahui ketidakseimbangan pada kolom target (Churn) cukup signifikan. Dengan  `No` sebanyak 5163 dan `Yes` sebesar mendekati 2000 ')
    
    # Membuat Garis Lurus
    st.markdown('---')
    
    # Membuat piechart
    st.write('### Menampilkan visualisasi pie chart untuk presentase kolom target No Churn & Churn')
    fig = plt.figure(figsize=(8,8), facecolor='white')
    df['Churn'].value_counts().plot(kind='pie', labels = ['',''], autopct='%1.1f%%', colors = ['darkslateblue','teal'])
    plt.legend(labels=['No', 'Yes']);
    st.pyplot(fig)
    st.write('Dari informasi visualisasi kolom target diatas, diketahui ketidakseimbangan pada kolom target (Churn) cukup signifikan. Dengan  `No` sebesar 73% dan `Yes` sebesar 27%, sehingga perlu diseimbangkan nantinya.')
    
    # Membuat Garis Lurus
    st.markdown('---')   

    # Membuat countplot
    st.write('### Distribusi Senior Citizen berdasarkan Churn')
    fig = plt.figure(figsize=(6,6), facecolor='white')
    sns.countplot(data=df, x='SeniorCitizen', hue='Churn', palette='viridis')
    plt.bar_label(plt.gca().containers[0])
    plt.bar_label(plt.gca().containers[1])
    plt.xticks([1,0], ['senior', 'bukan senior']);
    st.pyplot(fig)
    st.write('Dari visualisasi countplot diatas, melihat perbandingan SeniorCitizen dengan variabel target Churn, dimana yg senior sedikit melakukan chrun dari pada yg tidak churn, pelanggan senior mungkin telah terbiasa dengan tata cara penggunaan layanan tersebut dan merasa sulit untuk beralih ke layanan yang berbeda. Mereka mungkin tidak ingin menghadapi kerumitan dalam mempelajari layanan baru.')

    # Membuat Garis Lurus
    st.markdown('---')

    # Membuat subplot
    st.write('### Hubungan kolom Target (Churn) dengan kolom Monthly Charges, Total Charges & Tenure')
    fig = plt.figure(figsize=(15, 8))
    st.image('churn_fitur.png')
    st.write('Dari visualisai kolom eduaction level dengan default_payment_next_month, dapat melihat perbandingan jumlahnya di setiap kategori tingkat pendidikan. Ini memberikan informasi tentang seberapa sering default payment terjadi dalam setiap kelompok pendidikan.')

    # Membuat Garis Lurus
    st.markdown('---')

    # Membuat countplot
    st.write('### Distribusi Internet Service berdasarkan Churn')
    fig = plt.figure(figsize=(12, 6))
    sns.countplot(x='InternetService', hue='Churn', data=df)
    plt.bar_label(plt.gca().containers[0])
    plt.bar_label(plt.gca().containers[1])
    st.pyplot(fig)
    st.write('Dari informasi visualisasi diatas bahwa distribusi data yang Churn paling banyak yiatu dengan layanan internet Fiber Optic. Perusahaan dapat mengevaluasi kualitas layanan Fiber Optic atau mempertimbangkan untuk meningkatkan promosi atau penawaran khusus untuk mempertahankan pelanggan.')
    
    # Membuat Garis Lurus
    st.markdown('---')

    # Membuat subplot
    st.write('### Menvisualisasikan Partner & Dependents dengan kolom target')
    fig = plt.figure(figsize=(15, 4))
    st.image('partner_dependents.png')
    st.write('Dari visualisasi diatas diperoleh bahwa pelanggan yang tidak memiliki pasangan dan tanggungan mungkin memiliki prioritas dan preferensi yang berbeda dalam penggunaan layanan. Jika layanan tersebut tidak memenuhi kebutuhan dan preferensi mereka dengan baik, mereka cenderung untuk mencari alternatif yang lebih sesuai, sedangkan pelanggan yang memiliki pasangan dan tanggungan mungkin memiliki stabilitas finansial yang lebih tinggi, yang membuat mereka lebih mampu untuk membayar biaya langganan secara teratur.')

if __name__== '__main__':
    run()