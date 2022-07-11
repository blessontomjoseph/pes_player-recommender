from sklearn.impute import SimpleImputer
import numpy as np

def team_val(team_data):
    """finds the vector representing a team

    Args:
        team_data (dataframe): data containing only a teams info

    Returns:
        vector : team vector
    """
    weight=team_data.weight_val
#     ini_features = team_data.drop('weight_val',axis=1).select_dtypes('number')
    ini_features = team_data.select_dtypes('number')
    weighted_matrix = ini_features.apply(lambda x:x*weight)
    vector = weighted_matrix.sum(axis=0)
    normalized_vector = vector/(np.linalg.norm(vector))
    return normalized_vector.values


def pos_val(team_data,unique_position):
    """vector reprsenting  a position in a team

    Args:
        team_data (dataframe): data rrepresenting a team
        unique_position (series): all unique positions in a team

    Returns:
        vector: vector representing a position in a team
    """
    pos_data=team_data.loc[team_data['registered_position']==unique_position]
    weight=pos_data.weight_val
#     ini_feat=pos_data.drop('weight_val',axis=1).select_dtypes('number')
    ini_feat=pos_data.select_dtypes('number')
    weighted_matrix= ini_feat.apply(lambda x:x*weight)
    vector=weighted_matrix.sum(axis=0)
    normalized_vector=vector/np.linalg.norm(vector)
    return normalized_vector.values


def player_val(team_data,player):
    """player vector

    Args:
        team_data (dataframe): teamdata
        player (int): single player index from data

    Returns:
        vctor: player vector
    """
    player_data=team_data.loc[team_data.name==player]
#     vec=player_data.drop('weight_val',axis=1).select_dtypes('number')
    vec=player_data.select_dtypes('number')
    n_vec=vec/np.linalg.norm(vec)
    return n_vec.values




def feature_eng(data,new_features):
    """fills up the ralatonal values between a player and all the positions"""
    
    teams=data.team_name.unique()
    for team in teams:
        team_dict={}
        positional_dict={}
        player_dict={}
        
        team_data = data.loc[data['team_name']==team] #data for a unique team 
        team_dict[team]= team_val(team_data)
    
        unique_positions=team_data.registered_position.unique()
        for position in unique_positions:
            positional_dict[position]=pos_val(team_data,position)
        
        for ind in range(len(team_data)):
            name=team_data['name'].iloc[ind]
            player_dict[name]=player_val(team_data,name)
            
        for player in player_dict:
            new_features['Team'][new_features['name']==player] = np.linalg.norm(team_dict.get(team)-player_dict.get(player))

            for position in positional_dict:
                new_features[position][new_features['name']==player] = np.linalg.norm(positional_dict.get(position)-player_dict.get(player))
    
    return new_features


def fill_new_features(data,new_features):
    """fills the new_feature values

    Args:
        data (dataframe): preprocessed data
        new_features (dataframe): new_feature values to be filled

    Returns:
        dataframe: filled new_Features
    """
    new_features=feature_eng(data,new_features)
    im=SimpleImputer(missing_values=0,strategy='mean')
    num=new_features.select_dtypes('number').columns
    new_features[num]=im.fit_transform(new_features[num])
    return new_features