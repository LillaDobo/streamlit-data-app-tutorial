import pandas as pd
import numpy as np
import streamlit as st

st.title('Sales')
st.header('Data gathered')

data_load_state= st.text("Loading data...")
@st.cache_data
def data_load(nrows):
    data = pd.read_csv("salesdata.csv",nrows=nrows)
    data["Order Date"] = pd.to_datetime(data["Order Date"],dayfirst=True)
    data["Ship Date"] = pd.to_datetime(data["Ship Date"],dayfirst=True)
    return data
data_load_state= st.text("Done!")
data = data_load(9800)

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)

st.divider()

month_to_filter = st.slider('Month',1,12,4)




