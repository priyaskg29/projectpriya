from email.mime import image


import numpy as np
import pandas as pd
dataset=pd.read_csv('')
dataset
from sklearn import preprocessing 
le=preprocessing.LabelEncoder()
dataset['outlook']=le.fit_transform(dataset.outlook)
dataset['temp']=le.fit_transform(dataset.temp)
dataset['humidity']=le.fit_transform(dataset.humidity)
dataset['playgolf']=le.fit_transform(dataset.playgolf)
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,5].values
from sklearn.preprocessing 
