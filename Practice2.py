import random
import os

# Data structures practice

#Creating a list of my five top favorite food
# favorite_foods = []
# for i in range (5):
#     food = input("What is your favourite food?: ")
#     favorite_foods.append(food)

# print(favorite_foods[1])


# #Creating a dictionary to store my favorite book features
# title =  input("What is favourite book title? ")
# author = input("What is is author? ")
# genre = input("What is its genre? ")
# favourite_book = {
#     "title": title,
#     "author": author,
#     "genre": genre
# }

# print(favourite_book)

#Creating a random set
list =  [random.randint(1,10) for i in range(8)]
numbers = set(list)

# print(numbers)


# Global scope
global_variable = "global"  #3rd scope

def outer_func():
    # Nonlocal scope
    nonlocal_variable = "nonlocal"
    def inner_func():
        # Local scope
        local_variable = "local"
        print(f"Hi from the '{local_variable}' scope!") #1st scope Local
        print(f"Hi from the '{nonlocal_variable}' scope!") #2nd scope Enclosing
        print(f"Hi from the '{global_variable}' scope!") #3rd scope Global
    inner_func()


#Working on Error handling 

filename = input("Enter the name of the file: ")
try: 
    with open(filename, 'r'):
        pass
except FileNotFoundError as e:
    print(f"Sorry, the file you are looking for is not found. {e}")

