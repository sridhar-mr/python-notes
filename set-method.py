# SET

# unorder mutable dupilicate not allow ---> {} --> in set there no index so we can't update but we can add and remove

uber_cities1 = {"chennai", "tambaram", "guduvancherry","hyd"}
uber_cities2 = {"poonthamalle", 'avadi',"hyd"}

# uber_cities= set(uber_cities)
# print(uber_cities)


# union() ---> means it will add both give as a one output
print(uber_cities1.union(uber_cities2))

#intersection ---> means it will give commonly value from the item
print(uber_cities1.intersection(uber_cities2))

# difference() --> it will different value from the item
print(uber_cities1.difference(uber_cities2))

#add()
uber_cities1.add("SP kovil")
print(uber_cities1)


#remove()
uber_cities1.remove("chennai")
print(uber_cities1)


#discard() #--> it will cheack and remove value  if value is no there it will don't show error
uber_cities1.discard("goa")
print(uber_cities1)