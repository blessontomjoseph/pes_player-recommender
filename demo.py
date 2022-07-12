import utility
import pandas as pd

path= r"result\result.csv"
new_features = pd.read_csv(path)
filters = utility.streamlit(new_features)
utility.execute(filters, new_features)



