import utility
import pandas as pd
import streamlit as st

path = "result_data.csv"
ml_results = pd.read_csv(path)
filters = utility.streamlit(ml_results)
utility.ex(filters, ml_results)
