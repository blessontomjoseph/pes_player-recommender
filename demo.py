import utility
import pandas as pd
import streamlit as st

path = 'result_data.csv'
ml_results = pd.read_csv(path)
filters = utility.streamlit(ml_results)
similar = st.sidebar.button(
    label='apply', on_click=utility.ex(filters, ml_results))
st.write(similar)
