import utility
import streamlit as st
import pandas as pd

path='E:\kaggle\projects\feature eng PES\pes_player-recommender\result_data.csv'
ml_results=pd.read_csv(path)
filters=utility.streamlit(ml_results)
utility.ex(filters,ml_results)

