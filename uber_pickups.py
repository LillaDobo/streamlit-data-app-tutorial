import pandas as pd
import numpy as np
import streamlit as st

#cím
st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time' # változó típus oszlop elnevezés
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz') #adatok elérési linkjét tartalmazó változó

@st.cache_data # adatok gyorsabb betöltése nem kell mindig előről betölteni
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows= nrows) # csv beolvasás url-ból 
    lowercase = lambda x: str(x).lower() # kisbetűssé és szöveggé tétel
    data.rename(lowercase,axis='columns', inplace=True) # átnevezés
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN]) # meg felelő típussá alakítás
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000) # betöltés
data_load_state.text('Loading data...done!')

if st.checkbox('Show raw data'): # checkbox bepipálása akkor megjeleníti
    st.subheader('Raw data')
    st.write(data)


st.subheader('Number of pickups by hours')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24,range=(0,24))[0]
#gyakorisági sor ahol az órákat nézzük egy napban
st.bar_chart(hist_values) # oszlop diagram

# st.subheader('Map of all pickups')
# st.map(data)

hour_to_filter = st.slider('hour',0,23,17) # min: 0h, max: 23h, default:17h)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter] # megfelelő adatok kiválasztása
st.subheader(f'Maps of all pickoups at {hour_to_filter}:00')
st.map(filtered_data) # térkép megjelíntés


