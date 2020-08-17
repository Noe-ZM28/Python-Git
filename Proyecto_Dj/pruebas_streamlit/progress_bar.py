import streamlit as st 

import numpy as np
import pandas as pd 
import time

'Iniciando..'

latest_interation = st.empty()
bar = st.progress(0)


for i in range(100):
    latest_interation.text(f' {i +1}% de 100%')
    bar.progress(i +1)
    time.sleep (0.1)

'Inicio completado!'