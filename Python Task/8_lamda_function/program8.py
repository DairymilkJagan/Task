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
