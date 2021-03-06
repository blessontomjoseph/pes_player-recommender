import preprocessing
import features
import utility


data_path = r"data\pes2021-all-players.csv"
regular, new_data = preprocessing.pre(data_path) 
data_eng = features.new_features(regular, new_data)
player_name = input('player_name?')
similar_players = utility.similar_players(player_name, data_eng)
print(similar_players)
