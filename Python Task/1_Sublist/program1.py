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