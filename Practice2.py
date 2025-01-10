# Data structures practice

#Creating a list of my five top favorite food
favorite_foods = []
for i in range (5):
    food = input("What is your favourite food?: ")
    favorite_foods.append(food)

print(favorite_foods[1])


#Creating a dictionary to store my favorite book features
title =  input("What is favourite book title? ")
author = input("What is is author? ")
genre = input("What is its genre? ")
favourite_book = {
    "title": title,
    "author": author,
    "genre": genre
}

print(favourite_book)

#Creating
