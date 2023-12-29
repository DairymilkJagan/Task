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
