import pandas as pd
import numpy as np
from sklearn.preprocessing import  OrdinalEncoder, StandardScaler
from sklearn.impute import SimpleImputer


def pre(data_path):
    """data preprocessing

    Args:
        data_path (string)): path-unprocessed data
    """
    
    df= pd.read_csv(data_path)
    data=df.copy()

    data.drop('rating_stars',1,inplace=True)
    dic={'---':0}
    data['playing_style'].replace(dic,inplace=True)

    na=data.isna().sum()
    nan_cols=na[na>0].index
    # these rows has nan values
    
    im=SimpleImputer(strategy='median')
    data[nan_cols] =im.fit_transform(data[nan_cols])

    #foot
    foot_dict={'Left foot':0,'Right foot':1}
    data.foot_val=data.foot
    data.foot_val=data.foot.map(foot_dict)
    data['reg_pos_num'] = data.registered_position

    oe=OrdinalEncoder(categories=[['E','D','C','B','A'],
                                ['CF','RWF', 'LWF', 'SS','AMF', 'RMF', 'LMF','CMF','DMF','RB', 'LB', 'CB','GK'],
                                ['Creative Playmaker', 'Prolific Winger', 'Goal Poacher',
                              'Defensive Goalkeeper', 'Build Up', 'Extra Frontman',
                              'Offensive Goalkeeper', 'Anchor Man', 'Roaming Flank',
                              'Orchestrator', 'Hole Player', 'Box-to-Box', 'Offensive Full-back',
                              'The Destroyer', 'Dummy Runner', 'Fox in the Box',
                              'Classic No. 10', 'Target Man', 'Full-back Finisher',
                              'Defensive Full-back', 'Cross Specialist', 0]])

    data[['condition','reg_pos_num','playing_style']]=oe.fit_transform(data[['condition','reg_pos_num','playing_style']])

    numerical=data.select_dtypes('number').columns
    sc=StandardScaler()
    data[numerical]=sc.fit_transform(data[numerical])

    color=data.ball_color.unique()
    a=[i for i in range(5,0,-1)]
    mapper={color[i]:a[i] for i in range(5)}

    data['weight_val']=data['ball_color']
    data['weight_val']=data['ball_color'].map(mapper)
    categorical= data.select_dtypes('object').columns
    new_features=data[categorical]
#     data[['age']]
    extra=pd.DataFrame(np.zeros([new_features.shape[0],new_features.registered_position.unique().shape[0]+1]),columns=['RWF', 'LWF', 'CF', 'AMF', 'GK', 'CB', 'DMF', 'CMF', 'SS', 'LMF','RB', 'LB', 'RMF','Team'])
    new_features=pd.concat([new_features,extra],axis=1)  
    return data,new_features


