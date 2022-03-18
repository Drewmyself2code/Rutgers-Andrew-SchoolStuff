# -*- coding: utf-8 -*-
"""
Student Do: Grocery List.

This script showcases basic operations of Python Lists to help Sally
organize her grocery shopping list.
"""

# @TODO: Create a list of groceries
print("Grocery list:")
groceries = ['water', 'butter', 'eggs', 'apples', 'cinnamon', 'sugar', 'milk']
print(groceries)
print()


# @TODO: Find the first two items on the list
print("What are my first two items on the list?")
print(groceries[:2])
print()


# @TODO: Find the last five items on the list
print("What are all my items except for the first two?")
print(groceries[2:])
print()

# @TODO: Find every other item on the list, starting from the second item
print("What is every other item on the list, starting from the second item?")
print(groceries[1::2])
print()

# @TODO: Add an element to the end of the list
print("Oops, forgot to add flour...")
groceries.append("flour")
print(groceries)
print()

# @TODO: Changes a specified element within the list at the given index
print("I should be more specific with what kind of apples I want...")
groceries[3] = "gala apples"
print(groceries)
print()

# @TODO: Calculate how many items you have in the list
print("How many items do I have on my shopping list?")
print(len(groceries))
print()