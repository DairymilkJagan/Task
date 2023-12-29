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