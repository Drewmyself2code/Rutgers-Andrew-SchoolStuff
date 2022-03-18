## Apple Pie Ingredients


# @TODO: Create a list of groceries
print("Grocery List:")
groceries = ['water', 'butter', 'eggs', 'apples', 'cinnamon', 'sugar', 'milk']
print(groceries)
print()


# @TODO: Find the first two items on the list
print("What are the first two items on my list?")
print(groceries[:2])
print()

# @TODO: Find the last five items on the list
print("What are the last five items on my list?")
print(groceries[2:])
print()

# @TODO: Find every other item on the list, starting from the second item
print("What is every other item on my list, starting from the second item?")
print(groceries[1::2])
print()

# @TODO: Add an element to the end of the list
print("Oopsie poopsie, forgot to add flour...")
groceries.append("flour")
print(groceries)
print()

# @TODO: Changes a specified element within the list at the given index
print("I should be more specific with what kind of apples I want...")
index = groceries.index("apples")
groceries[index] = "gala apples"
print(groceries)
print()

# @TODO: Calculate how many items you have in the list
print("How many items do I have on my list?")
print(len(groceries))
print()

# ----------------------Go to the grocery store---------------------------")
print("*walks long distance to grocery store with a peg-leg 'send help'*")
print()

# @TODO: Find the index of the particular element name
print("Where can I find gala apples on my list?")
index = groceries.index("gala apples")
print(index)
print()

# @TODO: Remove an element from the list based on the given element name
print("Hang on, I remember I already have sugar...")
groceries.remove("sugar")
print(groceries)
print()

# @TODO: Remove an element from the list based on the given index
print("Oh wait, silly me, I also have water at home...")
index = groceries.index("water")
groceries.pop(index)
print(groceries)
print()


# @TODO: Remove the last element of the list
print("Seems I have only purchased the last item on my list. How fortunate for my peg-leg trip home...")
item = groceries.pop()
print("removed item = " + item)
print(groceries)
print()

print("You continue on your journey purchasing groceries...")
