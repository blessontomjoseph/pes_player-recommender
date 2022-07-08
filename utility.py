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

    

# def age_below(age,similar):
#     similar=similar.loc[similar['age']<age] 
#     return similar
    
def league(league,similar):
    similar=similar.loc[similar.league==league]
    return similar

# def current_team(self,team):
#     self.result=self.result.loc[self.result.team_name==team]
#     return self.result

def nationality(nationality,similar):
    similar=similar.loc[similar.nationality==nationality]
    return similar

def foot(foot,similar):
    similar=similar.loc[similar.foot==foot]
    return similar
    
def ball_color(ball_color,similar):
    similar=similar.loc[similar.ball_color==ball_color]
    return similar

def position (position,similar):
    similar=similar.loc[similar.registered_position==position]
    return similar

def ex(filters,new_data):
    # our_player=data.loc[data.name.str.contains(filters['player_name'].upper())]
    similar_player=similar_players(filters['player_name'],new_data)
    result=similar_player
    # if filters['age']!='no filter':
    #     result=age_below(filters['age'],similar_player)
    if filters['league']!='no filter':
        result=league(filters['league'],similar_player)
    if filters['nationality']!='no filter':   
        result=nationality(filters['nationality'],similar_player)
    if filters['foot']!='no filter':
        result=foot(filters['foot'],similar_player)
    if filters['ball_color']!='no filter':
        result=ball_color(filters['ball_color'],similar_player)
    if filters['position']!='no filter':
        result=position(filters['position'],similar_player)
    st.write(result)

    

def streamlit(new_data):    
    "take the result out as new_data"
    
    st.title('Player Recommendation')
    player_name = st.text_input("",key='search')
    button_clicked = st.button("ok")
    st.sidebar.title('Filter Items')
    
    # age=st.sidebar.slider('Age Below',15,50)
    league=st.sidebar.selectbox('League',['no filter']+list(new_data.league.unique())) # a filter of a league
    nationality=st.sidebar.selectbox('Nationality',['no filter']+list(new_data.nationality.unique())) #if result=empyu make apro result
    foot=st.sidebar.selectbox('foot',['no filter','Left','Right'])
    ball_color=st.sidebar.selectbox('Ball Color',['no filter']+list(new_data.ball_color.unique()))
    position=st.sidebar.selectbox('Position',['no filter']+list(new_data.registered_position.unique()))
    fils=['player_name','league','nationality','foot','ball_color','position']
    vals=[player_name,league,nationality,foot,ball_color,position]
    filter_pairs={fils[i]:vals[i] for i in range(len(fils)) if vals[i]!='no filter'}
    return filter_pairs
