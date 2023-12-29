# 1. Extend nested list by adding the sublist
# input: 
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# # sub list to add
# sub_list = ["h", "i", "j"]

# Expected output:
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list1 =["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
print(list1)

sub_list = ["h", "i", "j"]
print(sub_list)

#Extend the list 

list1[2][1][2].append(sub_list)
print(list1)

# 2. Convert two lists into a dictionary
# Input:
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# Expected Output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


keys = ['Ten', 'Twenty', 'Thirty' ,'forty']
values = [10, 20, 30 , 40]

# To create New Dictionary
c={}

for i in range(len(values)):
    c[keys[i]] = values[i]
print(c)

# 3. Delete a list of keys from a dictionary
# Input:
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# Keys to remove
# keys = ["name", "salary"]

# Expected Output:
#{'city': 'New york', 'age': 25}

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

print(sample_dict)

keys_to_delete = ["name", "salary"]
_ = [sample_dict.pop(key, None) for key in keys_to_delete]

# del sample_dict["name"]
# del sample_dict["salary"]

print("update = \n", sample_dict)

# 4. Rename key of a dictionary
# Input:
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# Expected Output:
# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}


sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

print(sample_dict)
sample_dict["name"] = "jagan"
# sample_dict["name"] = sample_dict.pop("name")
print(sample_dict)

# 5. Get the key of a minimum value from the following dictionary
# Input: 
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }

# Expected output:
# Math

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(min(sample_dict))
# print(min(sample_dict, key=sample_dict.get))

# 6.Read a file and pass it to a function which checks for the given input string 
# ( case insensitive check).
# If the given string is found, the function should return True. 
# Create another function which will read the input file s and scan it to 
# get the count of each word in it. 
# After the process is completed print each word  along with the number of times 
# it occurred in the file.


class FileReader:
    @staticmethod
    def check_word(word):
        with open("file.txt", "r") as file:
            for line in file:
                if word in line:
                    return True
        return False

    @staticmethod
    def count_word(filename):
        count_words = {}
        with open(filename, 'r') as file:
            for line in file:
                for word in line.split():
                    count_words[word] = count_words.get(word, 0) + 1
        return count_words


# Check if a word is present in the file
word_to_check = "Hello"
if FileReader.check_word(word_to_check):
    print(f"The word '{word_to_check}' is present in the file.")
else:
    print(f"The word '{word_to_check}' is not present in the file.")

# Count occurrences of each word in the file
filename_to_count = "file.txt"
word_counts = FileReader.count_word(filename_to_count)
print("Word counts:", word_counts)

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

#iterrows
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

# Explore lambda functions in python.
# Explore the use cases of ‘for loops’ and lambda functions
# Write a program using lambda with map, filter, reduce functions.

from functools import reduce

def lambda_function():
    names = ["Jagan", "Guru", "Bharani", "Vijay","Gowtham","Jagan", "Ajay", "Abhinesh"]

    # Using a for loop to print each name //
    for name in names:
        print(name)

    # Using map with lambda to create a list of names
    mapped_names = list(map(lambda x: x, names))
    print(mapped_names)

    # more than one name is present
    Jagan_indices = [index for index, name in enumerate(names) if name == "Jagan"]
    print("Occurrences of 'Jagan':", Jagan_indices)

    # Using filter with lambda to filter names containing the letter 'a'
    names_with_A = list(filter(lambda x: 'a' in x, names))
    print("Names containing 'A':", names_with_A)

    # Using reduce with lambda to concatenate all names
    char_count = reduce(lambda acc, curr : acc + len(curr), names,0)
    print(char_count)

    concatenated_names = reduce(lambda x, y: x + " " + y, names)
    print("Concatenated names:", concatenated_names)

if __name__ == "__main__":
    lambda_function()

#lambda Basics :
            #lambda function  // a simple 1-line function
            #do not use def or return keywords. these are implicit
            #apply same function to each element of a sequnces  // return the modified list

from functools import reduce

def squared(num): 
# squared = lambda num : num * num
    return num * num

print(squared(2))

def addTwo(num): 
# addTwo = lambda num : num + 2
    return num + 2

print(addTwo(12))

def sum_total(a,b):
# sum = lambda a, b : a + b
    return a+b

print(sum_total(10,10))

################################

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

################################ map funtion

numbers = [2,4,6,8,10,15,20]

squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))

################################ filter  method


odd_nums = filter(lambda num : num % 2 != 0 , numbers)

print(list(odd_nums))

######################### reduce
numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr : acc + curr, numbers)

print(total)

print(sum(numbers))

names = ['jagan','bharani','logesh','vijay','ajay','guru mohan','jaganajayguruvijay']

char_count = reduce(lambda acc, curr : acc + len(curr), names,0)

print(char_count)

##################################

def lambda_function():

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Using a for loop to print each number
    for number in numbers:
        print(number)

    # Using map with lambda to create a list of numbers
    mapped_numbers = list(map(lambda x: x, numbers))
    print(mapped_numbers)

    # Using map with lambda to get the index of 5 in the list
    index_of_5 = list(map(lambda x: numbers.index(x) if x == 5 else None, numbers))
    print("Index of 5:", index_of_5)

    # Using filter with lambda to filter numbers greater than 5
    numbers_gt_5 = list(filter(lambda x: x > 5, numbers))
    print("Numbers greater than 5:", numbers_gt_5)

    # Using reduce with lambda to find the sum of all numbers
    sum_of_numbers = reduce(lambda acc, curr: acc + curr, numbers, 0)
    print("Sum of all numbers:", sum_of_numbers)

    # Using reduce with lambda to concatenate all numbers as strings
    concatenated_numbers = reduce(lambda acc, curr: acc + " " + str(curr), numbers, "")
    print("Concatenated numbers:", concatenated_numbers)

if __name__ == "__main__":
    lambda_function()

    lambda_function()


# 9 Explore the difference between sorted and sort functions.
# Write example programs using sort and sorted function and interpret.


# Original list of numbers
numbers = [4, 2, 7, 1, 9, 5]

# Using sorted() to create a new sorted list
sorted_numbers = sorted(numbers)

# Printing the original and sorted lists
print("Original list:", numbers)
print("Sorted list using sorted():", sorted_numbers)

# Original list of names
names = ["Jagan","Rahul", "Ajith", "Bharani", "Logesh", "Guru"]

# Using sort() to sort the list in-place
names.sort()

# Printing the original and sorted lists
print("Original list:", names)
print("Sorted list using sort():", names)

# 10. Create a Person class with attributes name and age. 
# Implement a method that prints a greeting with the person's name and age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello! My name is {self.name} and I am {self.age} years old.")

# Create an instance Person class
person1 = Person("Jagan", 23)

# Accessing attributes and calling the greet method
print(f"{person1.name}'s age is {person1.age}.")
person1.greet()



