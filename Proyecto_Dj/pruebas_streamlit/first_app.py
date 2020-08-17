import streamlit as st 

import numpy as np
import pandas as pd 

st.title('My first app')

st.write("Tratando de crear una tabla :D :")
st.write(pd.DataFrame({
    'Primera columna': [1, 2, 3, 4],
    'Segunda columna': [10, 20, 30, 40]
}))
