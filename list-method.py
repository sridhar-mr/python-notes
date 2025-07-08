# Ordered, changeable, allows
# duplicates
# --> use this sysmbole []


number = ["1","2","3","4","5","6","7","8","9"]


# LIST METHOD

# append()
number.append("10")
print("Append Method", number) #it will add the item in the last

# insert()
number.insert(3,"22") # it also add item but what position to be add  -->  #use 2 arrgurment
print("insert Method", number)

#remove()
number.remove("22")
print("remove Method", number) # remove the item particularly

#pop()
number.pop() # remove the item from last
print("pop Method", number)

#reverse()
number.reverse()   # reverse the item
print("reverse Method", number)

#count()
print("count Method", number.count("4")) #how many 4 is there in the item



#LIST SLICING

print("slicing Method", number[0:2]) # it will give the value but not take a last value
print("slicing Method", number[-3:]) # it will give the value but not take a last value

#LIST ITERATION

for i in number:
    print(i)


if "4" in number:
    print("yes")


# list changeable and updateable the item

number[3] = "55"
print(number)

# to check what are thr position in the items

for i,location in enumerate(number):
    print(i, location)

    