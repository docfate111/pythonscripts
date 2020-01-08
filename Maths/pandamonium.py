import pandas as pd
"""
Created on Wed May 30 20:43:19 2018

@author: tdwil
"""
songs={'Genre':['trap', 'edm', 'dubstep'], 'Bands':['WEAREFURY', 'LOSTSKY', 'bishu'], 'Songs':['fury', 'fearless', 'mystic'] }
songs_frame=pd.DataFrame(songs)
#creates dataframe from dictionary
x=songs_frame['Bands']
y=songs_frame['Genre', 'Bands']
first_item=songs_frame.ix[0,0]
other_item=songs_frame.ix[1, 'Songs']
z=songs_frame.dfix[0:2, 0:3]
#slice of data frame
songs_frame.dtypes()
#to check data types
songs_frame.describe(include="all")
#returns statistical summary for al rows
songs_frame.info()
#gives info
songs_frame.head()
#reads first 5 lines of dataframe
a=songs_frame['Bands'].unique()
#new row without any repeating variables
new_dataframe=songs_frame(songs_frame['Bands'])
#creates new dataframe with that column
