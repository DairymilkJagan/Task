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