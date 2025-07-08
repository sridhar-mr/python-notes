# Day 5: Loops in Python 


#  1. What are Loops?
'''
Loops are used when you want to repeat some code multiple times.

Two main loops in Python:

--> for loop

--> while loop
'''

#=========================================================================#

# For Loops 

# You use a for loop to go through a sequence (like list, string, or range of numbers).

'''
Syntax:

for item in sequence:
    # code block
'''

#=====================================================================#
# Using range()

# for i in range(5):
#     print(i)
    
# ---> range(n) means 0 to n-1


# range(start, end)

'''
for i in range(1, 6):
    print(i)
    ----> range(1, 6) → from 1 to 5 (end is excluded)
'''


#=====================================================#

# Loop through string

# for ch in "macha":
#     print(ch)


#=================================================#

#while Loop – Simple Explanation

# while loop runs as long as a condition is true

'''
while condition:
    # code block
'''

# Basic while loop

# i = 1
# while i <= 5:
#     print(i)
#     i += 1



#====================================================#
'''
break and continue
break → stop the loop entirely

continue → skip current iteration, go to next

'''


#===========================================#

# Nested Loop 

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)


#=========================================#

# Loop with else

'''
Python has a unique thing – else with loops!

for i in range(3):
    print(i)
else:
    print("Loop finished!")
'''