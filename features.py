import numpy as np



def team_val(team_data,numerical_cols):
    weight=team_data.weight_val.to_numpy().reshape(-1,1)
    ini_features = team_data[numerical_cols].to_numpy()
    weighted_matrix = weight*ini_features
    vector = weighted_matrix.sum(axis=0)
    normalized_vector = vector/(np.linalg.norm(vector))
    return normalized_vector

def pos_val(team_data,unique_position,num_cols):
    pos_data=team_data.loc[team_data['registered_position']==unique_position]
    weight=pos_data.weight_val.to_numpy().reshape(-1,1)
    ini_feat=pos_data[num_cols].to_numpy()
    weighted_matrix= weight*ini_feat
    vector=weighted_matrix.sum(axis=0)
    normalized_vector=vector/np.linalg.norm(vector)
    return normalized_vector

def player_val(team_data,numerical_cols,player):
    player_data=team_data.iloc[player]
    vec=player_data[numerical_cols].to_numpy()
    n_vec=vec/np.linalg.norm(vec)
    return n_vec



def feature_eng(data,new_data):
    
    num_cols=regular.dtypes!='object'
    num_cols=list(num_cols.index[num_cols])
    num_cols.remove('weight_val') #numerical columns
    teams=data['team_name'].unique() #unique team names
    
    for i in teams:
        team_dict={}
        positional_dict={}
        player_dict={}
        df = data.loc[data['team_name']==i] #data for a unique team 
       
        team_dict[i]= team_val(df,num_cols)
        unique_positions=df.registered_position.unique()
        
        for j in unique_positions:
            positional_dict[j]=pos_val(df,j,num_cols)
        
        for j in range(df.shape[0]):
            name=df['name'].iloc[j]
            player_dict[name]=player_val(df,num_cols,j)
            
        for j in player_dict:
            new_data['Team'][new_data['name']==j] = np.linalg.norm(team_dict.get(i)-player_dict.get(j))

            for k in positional_dict:
                new_data[k][new_data['name']==j] = np.linalg.norm(positional_dict.get(k)-player_dict.get(j))
    
    return new_data