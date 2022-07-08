import numpy as np
import streamlit as st

def similar_players(player_name,data):
    """gets similar players

    Args:
        player_name (str): players similar to
        data (df): data with all similarity features
        numerical_cols (): _description_

    Returns:
        df: similar players with relevant details
    """

    our_player=data.loc[data['name'].str.contains(player_name.upper())]
    our_player=our_player.select_dtypes('number')
    other_players= data.select_dtypes('number')
    distance= our_player - other_players
    distance=np.linalg.norm(distance,axis=1)
    out=data.copy()
    out['p2p_dist']=distance
    players=out.sort_values('p2p_dist',ascending=True)
    return players[['name', 'shirt_number', 'team_name', 'league', 'nationality', 'region','foot', 'registered_position', 'ball_color']].iloc[1:]

    

def streamlit(new_data):    
    "take the result out as new_data"
    
    st.title('knn objects in f- space')
    player_name = st.sidebar.text_input("",key='search')
    # button_clicked = st.button("ok")
    st.sidebar.title('Filter Items')
    # age=st.sidebar.slider('Age Below',15,50)
    league=st.sidebar.selectbox('League',['no filter']+list(new_data.league.unique())) # a filter of a league
    nationality=st.sidebar.selectbox('Nationality',['no filter']+list(new_data.nationality.unique())) #if result=empyu make apro result
    foot=st.sidebar.selectbox('foot',['no filter','Left foot','Right foot'])
    ball_color=st.sidebar.selectbox('Ball Color',['no filter']+list(new_data.ball_color.unique()))
    position=st.sidebar.selectbox('Position',['no filter']+list(new_data.registered_position.unique()))
    fils=['player_name','league','nationality','foot','ball_color','position']
    vals=[player_name,league,nationality,foot,ball_color,position]
    filter_pairs={fils[i]:vals[i] for i in range(len(fils))}
    return filter_pairs


def ex(filters,new_data):
    "fulters the values of fiter sidebars new_data is outputted data "
    
    similar=similar_players(filters['player_name'],new_data)
    
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
    return similar

