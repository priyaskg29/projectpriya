import numpy as np
import pandas as pd
dataset=pd.read_csv("")
dataset
from sklearn import preprocessing 
le=preprocessing.LabelEncoder()
outlook_encoded=le.fit_transform(dataset.outlook)
print(outlook_encoded)
temp_encoded=le.fit_transform(dataset.temp)
print(temp_encoded)
humidity_encoded=le.fit_transform(dataset.humidity)
wind_encoded=le.fit_transform(dataset.wind)
play_encoded=le.fit_transform(dataset.play)
dataset['outlook']=le.fit_transform(dataset.outlook)
dataset['temp']=le.fit_transform(dataset.temp)
dataset['humidity']=le.fit_transform(dataset.humidity)
dataset['wind']=le.fit_transform(dataset.wind)
dataset['play']=le.fit_transform(dataset.play)

