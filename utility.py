import numpy as np


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

def filter_results(data,**kwargs):
    for key,value in kwargs.items():
        data=data.loc[data[key].str.contains(value)]
        return data
    
class filter:
    def __init__(self,result):
        self.result=result
    def f_age_above(self,age):
        return self.result[self.result['age']>age] 
    def f_age_below(self):
        return self.result[self.result['age']<age]
    def f_league(self):
        pass
    def f_position(self):
        pass
    def
    
    
def spreadlit(result):
    import streamlit as st
    st.title('player recommendation')
    st.``
    