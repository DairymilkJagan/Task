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

