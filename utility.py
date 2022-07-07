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
    def age_above(self,age):
        return self.result=self.result[self.result['age']>age] 
    
    def age_below(self,age):
        self.rusult=self.result[self.result['age']<age]
        self.result
        
    def league(self,league):
        self.result=self.result.loc[self.result.league==league]
        return self.result
    
    def current_team(self):
        self.result=self.result.loc[]
        pass
    def nationality(self):
        pass
    def foot(self):
        pass
    def ball_color(self):
        pass
    def position (self):
        pass
    
    
def nofilter(data):
    return data

def team_of_league(league,data):
        return data.loc[data.league==league]['team'].unique()

def streamlit():
    st.title('Player Recommendation')
    selected = st.text_input("",key='search')
    button_clicked = st.button("ok")
    st.sidebar.title('Filter Items')
    age_below=st.sidebar.slider('Age Below',15,50)
    league=st.sidebar.selectbox('League',[])
    current_team=st.sidebar.selectbox('Team',list()) # a filter of a league
    nationality=st.sidebar.selectbox('Nationality',list()) #if result=empyu make apro result
    foot=st.sidebar.selectbox('foot',['Left','Right'])
    ball_color=st.sidebar.selectbox('Ball Color',['Black','Gold','Silver','Bronze','White'])
    position=st.sidebar.selectbox('Position',list])
