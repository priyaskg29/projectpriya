from operator import le
import pandas as pd
info={'Gender':['Male','Female','Male','Female','Female'],
'Position':['Head','Asst. Prof','Asst. Prof','Head','Asst. Prof']}
df=pd.DataFrame(info)
print(df)
from sklearn.processing import LabelEncoder
le=LabelEncoder()
gender_encoded=le.fit_transform(dt['Gender'])
encoded_position=le.fit_transform(dt['Position'])
df['Encoded_Gender']=gender_encoded
df['Encoded_Position']=encoded_position
print(df)