import pandas as pd
import numpy as np
import streamlit as st

path= r"result\result.csv"
new_features = pd.read_csv(path)

def streamlit(new_features):    
    "outputs filter options"
    
    st.title('Player Suggestions')
    # st.write('Results')
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

        
if __name__ == "__main__":
    filters = streamlit(new_features)
    execute(filters, new_features)


