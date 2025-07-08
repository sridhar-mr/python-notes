#TUPLE
# ---> () use this symbole

# order maintain and different data type we can pass and allow dupilication  -> immutuable--> cant change
# this was fast then list because we cant add remove

# number = ("1","2","3","4","5")
# print(number)

# print(number[2]) #--> index position check 



# print(len(number))  # ---> to find how many items in the tuple



# print(number.count(3))
# print(number.index("3"))




items = ("one", "two","three","four")
# We can use tuple in loops also
for i in items:
  print(i)

print(items[1])  # ---> Indexing the Values
print(items[1:3])  # --->  slicing
print(len(items))  # --> leanth of the items


# tuple to list and list to tuple
productList = list(items)
itemsTuple = tuple(productList)
print(type(productList))
print(type(itemsTuple))
