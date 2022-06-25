import pandas as pd
import numpy as np
from sklearn.preprocessing import  OrdinalEncoder, StandardScaler
from sklearn.impute import SimpleImputer
import warnings
warnings.simplefilter('ignore')



def pre(data_path):
  
  df= pd.read_csv(data_path)
  regular=df.copy()

  regular.drop('rating_stars',1,inplace=True)
  dic={'---':0}
  regular['playing_style'].replace(dic,inplace=True)

  na=regular.isna().sum()
  nan_cols=na[na>0].index
  # these rows has nan values
  im=SimpleImputer(strategy='median')
  regular[nan_cols] =im.fit_transform(regular[nan_cols])

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
  return regular,new_data
