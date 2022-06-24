import pandas as pd
import numpy as np
from sklearn.preprocessing import  OrdinalEncoder, StandardScaler
from sklearn.impute import SimpleImputer
import warnings
warnings.simplefilter('ignore')

data_path = 'pes2021-all-players.csv'
df= pd.read_csv(data_path)


# com = df.columns[df.columns.str.contains('com')]  #1 or 0 only smal num of players has com abilities
# skill = df.columns[df.columns.str.contains('skill')] # 1 or 0 only few of em has anny of the skills
# positions=['LWF','SS','CF','RWF','LMF','DMF','CMF','AMF','RMF','LB','CB','RB']
#unique positions,each players has a rating in every position from 0-2
# all_rating=df.columns[df.columns.str.contains('rating')]


regular=df.copy()
regular.drop('rating_stars',1,inplace=True)
dic={'---':0}
regular['playing_style'].replace(dic,inplace=True)

na=regular.isna().sum()
nan_cols=na[na>0].index
# these rows has nan values


im=SimpleImputer(strategy='median')
regular[nan_cols] =im.fit_transform(regular[nan_cols])


# python preprocessing.py


#foot
foot_dict={'Left foot':0,'Right foot':1}
regular.foot_val=regular.foot
regular.foot_val=regular.foot.map(foot_dict)
regular['reg_pos_num'] = regular.registered_position

# condition ='sort of current status'
#reg pos num the number curresponding to reistered position though the original coulumn needed as is.

oe=OrdinalEncoder(categories=[['E','D','C','B','A'],
                              ['CF','RWF', 'LWF', 'SS','AMF', 'RMF', 'LMF','CMF','DMF','RB', 'LB', 'CB','GK'],
                              ['Creative Playmaker', 'Prolific Winger', 'Goal Poacher',
                            'Defensive Goalkeeper', 'Build Up', 'Extra Frontman',
                            'Offensive Goalkeeper', 'Anchor Man', 'Roaming Flank',
                            'Orchestrator', 'Hole Player', 'Box-to-Box', 'Offensive Full-back',
                            'The Destroyer', 'Dummy Runner', 'Fox in the Box',
                            'Classic No. 10', 'Target Man', 'Full-back Finisher',
                            'Defensive Full-back', 'Cross Specialist', 0]])

regular[['condition','reg_pos_num','playing_style']]=oe.fit_transform(regular[['condition','reg_pos_num','playing_style']])


numerical=regular.select_dtypes('number').columns
sc=StandardScaler()
regular[numerical]=sc.fit_transform(regular[numerical])



color=regular.ball_color.unique()
a=[i for i in range(5,0,-1)]
mapper={color[i]:a[i] for i in range(5)}

regular['weight_val']=regular['ball_color']
regular['weight_val']=regular['ball_color'].map(mapper)
categorical= regular.select_dtypes('object').columns
new_data=regular[categorical]

extra=pd.DataFrame(np.zeros([new_data.shape[0],new_data.registered_position.unique().shape[0]+1]),columns=['RWF', 'LWF', 'CF', 'AMF', 'GK', 'CB', 'DMF', 'CMF', 'SS', 'LMF','RB', 'LB', 'RMF','Team'])
new_data=pd.concat([new_data,extra],axis=1)
print(new_data.head(5))



# 
# Host aws_ec2_first
#     HostName ec2-54-245-143-111.us-west-2.compute.amazonaws.com
#     IdentityFile C:\Users\USER\.ssh\aws_first_ec2.pem
#     User ec2-user