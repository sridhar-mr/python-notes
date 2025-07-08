# Key-value pairs, unordered, changeable
#it allow dupilicate but take the lastest kay and value

trip = {
    "person_name": ["Sridhar","Sandy","Oero"],
    "location": "Chennai",
    "person_there": 4,
    "fare": 300,
    "fare": 600

}

print(trip["fare"]) #when we call value using this error will throw

#get()
print("Get Method", trip.get("fare")) #when we use this to call value it will not show error it will give as a "NONE"
print("Get Method", trip.get("chennai")) #same was the value

#key()
print("Key Method", trip.keys()) #it will give all the key in the given item

#value()
print("Value Method", trip.values()) #it will give all the value in the given item

#items()
print("Item Method", trip.items()) #it will give a key and value pair


# dic Iteration

for key, value in trip.items():
    print(key," : ",  value) #it allow dupilicate but take the lastest kay and value

#update
trip.update({"days_of_trip":"6"})
print("Update Method", trip) #check the key if not there it will add --> if there means overwrite the key and value


#pop()
trip.pop("fare")
print("Pop Method", trip)


#we can access multiple value
print("We can access Multiple Value --- " , trip["person_name"][1])

#we can Iteration also

for i in trip["person_name"]:
    print(i)