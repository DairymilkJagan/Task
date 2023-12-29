#apply
#Explore the difference between iterrows(), itertuples(), apply(), map()
# Analyze the time taken for above operations using 
# one wider dataset(large no of columns) and one taller dataset(Large no. of rows)
# Read dataset as pandas dataframe
import pandas as pd
import time

data_1 = pd.read_csv(r"D:\Product Task\24.12.2023\7_Dataset\Scrobble_Features.csv")
df1 = pd.DataFrame(data_1)

# Generate a wider dataset
def generate_wider_dataset(num_rows, num_columns):
    data = {f'col_{_}': [i for i in range(num_rows)] for _ in range(num_columns)}
    return pd.DataFrame(data)

# Generate a taller dataset
def generate_taller_dataset(num_rows, num_columns):
    data = {f'col_{i}': [i for _ in range(num_columns)] for i in range(num_rows)}
    return pd.DataFrame(data)

# Function to measure time taken by iterrows() method
def measure_iterrows_time(df):
    start_time = time.time()
    
    # for index, row in df.iterrows():
    #     # Print row elements for inspection
    #     pass

    print(df1['Song'])

    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

# Generating wider and taller datasets
wider_dataset = generate_wider_dataset(1000, 1000)
taller_dataset = generate_taller_dataset(100000, 10)

# Analyzing time for iterrows() on the wider dataset
wider_time = measure_iterrows_time(wider_dataset)
print("Time taken for iterrows() on the wider dataset:", wider_time)

# Analyzing time for iterrows() on the taller dataset
taller_time = measure_iterrows_time(taller_dataset)
print("Time taken for iterrows() on the taller dataset:", taller_time)
import pandas as pd
import time

#Making DataFrame from CSV file
data_1 = pd.read_csv(r"D:\Product Task\24.12.2023\7_Dataset\Scrobble_Features.csv")
df1 = pd.DataFrame(data_1)

# Create a wider dataset // (large number of columns)
wide_data = {'col' + str(i): range(1000) for i in range(1000)}
wide_df = pd.DataFrame(wide_data)

# Create a taller dataset // (large number of rows)
tall_data = {'col': range(1000000)}
tall_df = pd.DataFrame(tall_data)

def apply(df):
    print(df1.apply(lambda row: row["Performer"], axis=1)) # Print the entire row for inspection

    # return x * 2
    # print(df1.apply(lambda row: row['song'], axis=1))

def time_apply(df1, func):
    start_time = time.time()
    result = df1.apply(func)
    end_time = time.time()
    return result, end_time - start_time

# Analyze time 
result_wide, time_wide = time_apply(wide_df, apply)
print(f"Time taken for applying on wider dataset: {time_wide:.5f} seconds")

# Analyze time
result_tall, time_tall = time_apply(tall_df, apply)
print(f"Time taken for applying on taller dataset: {time_tall:.5f} seconds")