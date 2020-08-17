import streamlit as st 

import numpy as np
import pandas as pd 



df = pd.DataFrame({
  'Primer columna': [1, 2, 3, 4],
  'Segunda columna': [10, 20, 30, 40]
})

df

option = st.selectbox(
    '¿Que numero te gusta mas de la primer columna?',
    df['Primer columna'])
'Seleccionaste: ', option

option = st.selectbox(
    '¿Que numero te gusta mas de la segunda columna?',
    df['Segunda columna'])
'Seleccionaste: ', option
