import preprocessing
import features
import utility

regular,new_data=preprocessing.data #something like this
data_eng = features.new_features(regular,new_data)

player_name=input('player_name?')
# filters=input('filters?(league/nationality/foot)if no filters type all')

similar=utility.similar_players(data_eng,player_name)
print(similar)