import streamlit as st
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

model = joblib.load('kmeans_model')
scaler = joblib.load('scaler_model')

st.title("customer segmentation app")
st.header('enter the monetary ,frequency and recency')
val1 = st.number_input("montetary")
val2 = st.number_input("frequency")
val3 = st.number_input("recency")

input_data = [val1,val2,val3]
pred = model.predict(scaler.transform([input_data]))[0]

if st.button('predict'):
	st.success(f'predicted cluster is :{pred}')
	
