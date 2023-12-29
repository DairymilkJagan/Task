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


