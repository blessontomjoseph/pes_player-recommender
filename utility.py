import numpy as np
import streamlit as st
from sklearn.preprocessing import MinMaxScaler

def similar_players(player_name,new_features):
    """gets similar players

    Args:
        player_name (str): players similar to
        new_features (df): new_features with all similarity features
        numerical_cols (): _description_

    Returns:
        df: similar players with relevant details
    """
    mm=MinMaxScaler(feature_range=(0,1))
    our_player=new_features.loc[new_features['name']==player_name]
    our_player=our_player.select_dtypes('number').to_numpy()
    other_players= new_features.select_dtypes('number').to_numpy()
    diss=np.linalg.norm((our_player - other_players),axis=1)
    out=new_features.copy()
    out['similarity']=diss #similarity=p2p_dist
    out['similarity']=1-mm.fit_transform(out['similarity'].to_numpy().reshape(-1,1)) 
    players=out.sort_values('similarity',ascending=False)
    return players[['similarity','name', 'shirt_number', 'team_name', 'league', 'nationality', 'region','foot', 'registered_position', 'ball_color']].iloc[1:]
    
    

def streamlit(new_features):    
    "outputs filter options"
    
    st.title('Find Similar Players')
    st.write('Results')
    st.sidebar.title('Find Players Like..')
    # player_name = st.sidebar.text_input("",key='search')
    # button_clicked = st.sidebar.button("ok")
    player_name=st.sidebar.selectbox('Player',['Player Name']+sorted(list(new_features.name)))
    st.sidebar.title('Filter Items')
    # age=st.sidebar.slider('Age Below',15,50)
    league=st.sidebar.selectbox('League',['no filter']+list(new_features.league.unique())) # a filter of a league
    nationality=st.sidebar.selectbox('Nationality',['no filter']+list(new_features.nationality.unique())) #if result=empyu make apro result
    foot=st.sidebar.selectbox('Foot',['no filter','Left foot','Right foot'])
    ball_color=st.sidebar.selectbox('Ball Color',['no filter']+list(new_features.ball_color.unique()))
    position=st.sidebar.selectbox('Position',['no filter']+list(new_features.registered_position.unique()))
    fils=['player_name','league','nationality','foot','ball_color','position']
    vals=[player_name,league,nationality,foot,ball_color,position]
    filter_pairs={fils[i]:vals[i] for i in range(len(fils))}
    return filter_pairs


def execute(filters,new_features):
    "filters the values of fiter sidebars and prints similar players "
    if st.sidebar.button('apply'):
    
        similar=similar_players(filters['player_name'],new_features)
        
        # if filters['age']!='no filter':
        #     result=age_below(filters['age'],similar_player)
        
        if filters['league']!='no filter':
            similar=similar.loc[similar.league==filters['league']]
            
        if filters['nationality']!='no filter':   
            similar=similar.loc[similar.nationality==filters['nationality']]
            
        if filters['foot']!='no filter':
            similar=similar.loc[similar.foot==filters['foot']]
            
        if filters['ball_color']!='no filter':
            similar=similar.loc[similar.ball_color==filters['ball_color']]
            
        if filters['position']!='no filter':
            similar=similar.loc[similar.registered_position==filters['position']]
            
        similar.reset_index(drop=True,inplace=True)
        st.write(similar)
        

