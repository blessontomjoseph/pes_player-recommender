import pandas as pd

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.impute import SimpleImputer


data_path = ' '
df= pd.read_csv(data_path)


com = df.columns[df.columns.str.contains('com')]  #1 or 0 only smal num of players has com abilities
skill = df.columns[df.columns.str.contains('skill')] # 1 or 0 only few of em has anny of the skills
positions=['LWF','SS','CF','RWF','LMF','DMF','CMF','AMF','RMF','LB','CB','RB']
#unique positions,each players has a rating in every position from 0-2
all_rating=df.columns[df.columns.str.contains('rating')]



regular=df.copy()
teams=regular.team_name.unique()

regular.rating_stars.unique()
regular.drop('rating_stars',1,inplace=True)

dic={'---':0}
regular['playing_style'].replace(dic,inplace=True)

na=regular.isna().sum()
nan_cols=na[na>0].index
# these rows has nan values

im=SimpleImputer(strategy='median')
nans=regular[nan_cols]   # all the nan values cols taken and imputed and replaced them in the original data
nans=pd.DataFrame(im.fit_transform(nans),columns=nans.columns)
regular[nan_cols]=nans


#foot
foot_dict={'Left foot':0,'Right foot':1}
regular.foot_val=regular.foot
regular.foot_val=regular.foot.map(foot_dict)

regular['reg_pos_num'] = regular.registered_position

# condition ='sort of current status'
#reg pos num the number curresponding to reistered position though the original coulumn needed as is.

oe=OrdinalEncoder(categories=[['E','D','C','B','A'],['CF','RWF', 'LWF', 'SS','AMF', 'RMF', 'LMF','CMF','DMF','RB', 'LB', 'CB','GK'],['Creative Playmaker', 'Prolific Winger', 'Goal Poacher',
       'Defensive Goalkeeper', 'Build Up', 'Extra Frontman',
       'Offensive Goalkeeper', 'Anchor Man', 'Roaming Flank',
       'Orchestrator', 'Hole Player', 'Box-to-Box', 'Offensive Full-back',
       'The Destroyer', 'Dummy Runner', 'Fox in the Box',
       'Classic No. 10', 'Target Man', 'Full-back Finisher',
       'Defensive Full-back', 'Cross Specialist', 0]])
regular[['condition','reg_pos_num','playing_style']]=oe.fit_transform(regular[['condition','reg_pos_num','playing_style']])

categorical=[]
for i in regular.columns:
    if regular[i].dtype=='object':
        categorical.append(i)
categorical    
columns=regular.columns

numerical=[i for i in columns if i not in categorical]
num_data=regular[numerical]
sc=StandardScaler()
num_data=pd.DataFrame(sc.fit_transform(num_data),columns=num_data.columns)

appender=regular[categorical]
appender.reset_index(drop=True,inplace=True)
num_data.reset_index(drop=True,inplace=True)
regular=pd.concat([appender,num_data],axis=1)

team=regular.team_name.unique()

color=regular.ball_color.unique()
a=[i for i in range(5,0,-1)]
mapper={color[i]:a[i] for i in range(5)}

regular['weight_val']=regular['ball_color']
regular['weight_val']=regular['ball_color'].map(mapper)

new_data=regular.iloc[:,:9]
new_data.registered_position.unique()

extra=pd.DataFrame(np.zeros([new_data.shape[0],new_data.registered_position.unique().shape[0]+1]),columns=['RWF', 'LWF', 'CF', 'AMF', 'GK', 'CB', 'DMF', 'CMF', 'SS', 'LMF',
       'RB', 'LB', 'RMF','Team'])
new_data=pd.concat([new_data,extra],axis=1)