import preprocessing
import features
import pandas as pd

data_path = 'pes2021-all-players.csv'
regular,new_data=preprocessing.pre(data_path) #something like this
data_eng = features.new_features(regular,new_data)
data_eng.to_csv('result_data.csv',header=True,index=False)
