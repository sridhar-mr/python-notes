#Day 7: Data Structures

#1. List – 🔢 Ordered, changeable, allows duplicates --->  []



product = ["Note", "Pen", 'table', 'classroom', 'teacher', 'student' ]

print(product[2]) #-->Indexing
print(product[1:3]) #--> slicing
product.append("school") #---> add the value and end 
product.insert(4,"MAM") #--> add at any postion
product.remove("MAM") #--> Remove by value
product.pop(4)  #--> remove by index  --> if therer was no index given remove the last item

print(product)
print(len(product))



