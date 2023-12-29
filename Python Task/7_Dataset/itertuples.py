#itertuples
#Explore the difference between iterrows(), itertuples(), apply(), map()
# Analyze the time taken for above operations using 
# one wider dataset(large no of columns) and one taller dataset(Large no. of rows)
# Read dataset as pandas dataframe

import pandas as pd
import time

data_1 = pd.read_csv(r"D:\Product Task\24.12.2023\7_Dataset\Scrobble_Features.csv")
df1 = pd.DataFrame(data_1)

# Create a wider dataset (large number of columns)
wide_data = {'col' + str(i): range(1000) for i in range(1000)}
wide_df = pd.DataFrame(wide_data)

# Create a taller dataset (large number of rows)
tall_data = {'col': range(1000000)}
tall_df = pd.DataFrame(tall_data)

def time_itertuples(df):
    start_time = time.time()

    for row in df1.itertuples():
        print(getattr(row, 'Song'), getattr(row, 'valence'), getattr(row, 'spotify_track_id'))

    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print(f"Elapsed time: {elapsed_time} seconds")
    
    end_time = time.time()
    return end_time - start_time

# Analyze time 
time_wide = time_itertuples(wide_df)
print(f"Time taken for wider dataset: {time_wide:.5f} seconds")

# Analyze time
time_tall = time_itertuples(tall_df)
print(f"Time taken for taller dataset: {time_tall:.5f} seconds")
