#replacing missing data:
import pandas as pd
import numpy as np
#creating dataframe with missing values:
data=pd.DataFrame([[1, 2, np.nan], [np.nan, 2, np.nan], [3, np.nan, np.nan], [np.nan, 3, 8], [5, 3, np.nan]], columns=['A', 'B', 'C'])
print(data, '\n') #prints the data
#counts nan values for each feature
print(data.isnull().sum(axis=0))
#drops C from dataset:
data.drop('C', axis=1, inplace=True)
#creates a placeholder for B's missing values
data['missingB']=data['B'].isnull().astype(int)
#filling in missing items in B using B's average:
data['B'].fillna(data['B'].mean(), inplace=True)
#same with A:
data['A'].interpolate(method='linear', inplace=True)
print(data)

