import preprocessing
import features
import utility

regular,new_data=preprocessing.data #something like this
data_eng = features.new_features(regular,new_data)

player_name=input('player_name?')
filer=input('filters?(league/nationality/age_below/age_above/foot)')
similar=utility.similar_players(data_eng,player_name)
print(similar)