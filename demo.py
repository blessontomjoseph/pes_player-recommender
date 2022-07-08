import utility
import streamlit as st
import pandas as pd

path='result_data.csv'
ml_results=pd.read_csv(path)
print(ml_results.columns)


filters=utility.streamlit(ml_results)
utility.ex(filters,ml_results)

