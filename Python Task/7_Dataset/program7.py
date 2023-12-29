import pandas as pd

# making data frame from csv file
# df = pd.read_csv(r"D:\Product Task\24.12.2023\7_Dataset\employees.csv")
df = pd.read_csv(r"D:\Product Task\24.12.2023\7_Dataset\Scrobble_Features.csv")

# for data visualization
print(df)

# 1.using index method  
# Range index 0-1000

for index in df.index:
    print(df['SongID'][index],
          df['Performer'][index])
    
#2.using loc[] method
    
for index in range(len(df)):
    print(df.loc[index, 'Song'],
          df.loc[index, 'key'],
          df.loc[index, 'mode'])
    
# 3. using iloc[]method
    
for index in range(len(df)):
    print(df.iloc[index, 0],
          df.iloc[index, 1],
          df.iloc[index, 4],
          df.iloc[index, 5])
    
# #4. using iterrows() method
    
for i,r in df.iterrows():   #i in index //  r in row
    print(r['index'],  #row element of 1st name
          r['loudness'],
          r['valence'],
          r['liveness'])

# #5. using itertuples() method
    
for row in df.itertuples():    #keyword : get attributes 
    print(getattr(row, "index"),
          getattr(row, "Song"),
          getattr(row, "liveness"))
    
# #6. using apply() method
    
print (df.apply(lambda row: row["liveness"], axis=1))