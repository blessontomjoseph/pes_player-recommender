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
    other_players= data.select_dtypes('nuimber')
    distance= our_player - other_players
    distance=np.linalg.norm(distance,axis=1)
    out=data.copy()
    out['p2p_dist']=distance
    players=out.sort_values('p2p_dist',ascending=True)
    return players.select_dtypes('object').iloc[1:]

    
class filter:
    def __init__(self,result):
        self.result=result
        
    def age_below(self,age):
        self.result=self.result[self.result['player_age']<age] 
        return self.result
        
    def league(self,league):
        self.result=self.result.loc[self.result.league==league]
        return self.result
    
    def current_team(self,team):
        self.result=self.result.loc[self.result.team_name==team]
        return self.result
    
    def nationality(self,nationality):
        self.result=self.result.loc[self.result.nationality==nationality]
        return self.result
    
    def foot(self,foot):
        pass
    def ball_color(self):
        pass
    def position (self):
        pass

def streamlit(new_data):    
    st.title('Player Recommendation')
    player_name = st.text_input("",key='search')
    button_clicked = st.button("ok")
    st.sidebar.title('Filter Items')
    
    age=st.sidebar.slider('Age Below',15,50)
    league=st.sidebar.selectbox('League',['no filter']+list(new_data.league.unique())) # a filter of a league
    nationality=st.sidebar.selectbox('Nationality',['no filter']+list(new_data.nationality.unique())) #if result=empyu make apro result
    foot=st.sidebar.selectbox('foot',['no filter','Left','Right'])
    ball_color=st.sidebar.selectbox('Ball Color',['no filter']+list(new_data.ball_color.unique()))
    position=st.sidebar.selectbox('Position',['no filter']+list(new_data.registered_position.unique()))
    fils=['player_name','age','league','nationality','foot','ball_color','position']
    vals=[player_name,age,league,nationality,foot,ball_color,position]
    return {fils[i]:vals[i] for i in range(len(fils)) if vals[i]!='no filter'}
