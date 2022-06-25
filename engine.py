import preprocessing
import features
import utility


data_path = 'pes2021-all-players.csv'
regular,new_data=preprocessing.pre(data_path) #something like this
data_eng = features.new_features(regular,new_data)
print(data_eng.head(5))
# player_name=input('player_name?')
# # filters=input('filters?(league/nationality/foot)if no filters type all')

# similar=utility.similar_players(data_eng,player_name)
# print(similar)