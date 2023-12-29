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
