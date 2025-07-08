
# ================================= inheritance ============= #

# code reuseablility
# create a child class from a parent class
# Single Level inheritance
# we should create a object to last child

# from userYour_folder class_object.file_name import parent_name --> import from one to another


#Types of Python Inheritance
# Single Inheritance: A child class inherits from one parent class.
# Multiple Inheritance: A child class inherits from more than one parent class.
# Multilevel Inheritance: A class is derived from a class which is also derived from another class.
# Hierarchical Inheritance: Multiple classes inherit from a single parent class.
# Hybrid Inheritance: A combination of more than one type of inheritance.


# class grandfather:
#     def car(self):        #this was the Multilevel leve inheritance one parent two child we can access with the last child
#         print("car is red color")
#



class dad():
    def house(self):
        print("I am From dad Class")


class mom:
    def shop(self):
        print("shop color is red")


class daugther(dad,mom):  # when we use the two parent class in one child class that is multiple Inheritance
    def work(self):
        print("I am from daugther class")


class son(dad):  # when we use that dad inside son that make a relation
    def profit(self):
        print("I am From Son Class")

    # def house(self):     # we can overwite the parent from child
    #   print("I am Overwited ")



# class son2(dad): # Hierarchical Inheritance one parent to multiple child
#     def maket(self):
#         print(" i have market")


s = son()
# s2 = son2() #for Hierarchical Inheritance we create spearate two object
s.house()
s.profit()



