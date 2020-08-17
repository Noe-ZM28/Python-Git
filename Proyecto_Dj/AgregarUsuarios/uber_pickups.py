import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('Recogidas de Uber en NYC') #Titulos de la aplicacion de streamlit

progreso = st.empty()
barra = st.progress(0)


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache #usar cache (si existe) en ves de cargar datos cada ves que inicia
def load_data(nrows): #Wolo acepta como parametro nrows
    #nrows indica el numero de filas en el dataframe
    data = pd.read_csv(DATA_URL, nrows= nrows)
    lowercase = lambda x: str(x).lower()
    #lowercase = minusculas
    data.rename(lowercase, axis ='columns', inplace = True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

#Mensaje que indica que se estan cargando el dataframe
data_load_state = st.text('Cargando datos, espere un momento...')

#indicar que se usaran 10mil filas del dataframe
data = load_data(10000)

#barra de progreso simple
for i in range(100):
    progreso.text(f' {i +1}% de 100%')
    barra.progress(i +1)
    time.sleep (0.01)

#Modifica rle mensaje para indicar que se han agregado los datos
data_load_state.text('¡Datos cargados correctamente!')

#agrego un checkbox para que el usuario elija o no ver los datos en bruto
if (st.checkbox('Mostrar datos en bruto')):
    #Agrego un subtitulo
    st.subheader('Datos en bruto')
    #muestro el dataframe
    st.write(data)

#agrego un nuevo subttulo
st.subheader('Recogidas de Uber por Hora')

#crer el histograma
hist_values = np.histogram (
                            data[DATE_COLUMN].dt.hour,
                            bins = 24, 
                            range= (0, 24)
                            )[0]

#mostrar el histograma
st.bar_chart(hist_values)

#creo una lista desplegble  text/min/max/deafult
hour_to_filter = st.slider('Hora', 0, 23, 12)

#Filtramos las recogidas que concuerden con la hora en la lista desplegable
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

#agregar otro subtitulo 
st.subheader(f'Mapa de todas las recogidas en las {hour_to_filter}:00')

#grafico llos datos filtrados
st.map(filtered_data)
















