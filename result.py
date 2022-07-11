# result for streamlit demo

import preprocessing
import features

data_path = 'pes2021-all-players.csv'
data,new_features=preprocessing.pre(data_path) 
new_features = features.fill_new_features(data,new_features)
new_features.to_csv('result.csv',header=True,index=False)
