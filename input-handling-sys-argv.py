import sys


if len(sys.argv) == 2:
    print("usage: You should give full name and last name")
    sys.exit()  #--->this condition  to avoid error from that code



full_name = " ".join(sys.argv[1:]) #--> after the all index that use
print(full_name) #--> it will give like list that we should join can use join() it will come in same string
# full_name = sys.argv[1] #--> that 1 was index for given name
# last_name = sys.argv[2] #--> that 2 was index for given name
email = full_name.lower().replace(" ", ".")+ "@gmail.com"


print("------- YOUR PROFILE -------")

print(full_name)
print(email)
