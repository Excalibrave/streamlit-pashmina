import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

model = pickle.load(open('prediksi_jual.sav','rb'))

df = pd.read_excel("data_olah.xlsx")
df['Date'] = pd.to_datetime(df['Date'],format='%M')
df.set_index(['Date'], inplace=True)

st.title('Forecasting Penjualan Pashmina')
month = st.slider("Tentukan Bulan",1,6, step=1)

pred = model.forecast(month)
pred = pd.DataFrame(pred, columns=['Jumlah'])

if st.button("Prediksi"):
    
    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig, ax = plt.subplots()
        df['Jumlah'].plot(style='--', color='gray', legend=True, label='Known')
        pred['Jumlah'].plot(color='b', legend=True, label='Prediction')
        st.pyplot(fig)
        