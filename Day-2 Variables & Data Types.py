# Day-2 Variable and Data Types



# 1. What is a Variable?


'''Variable is like a container to store a value.
Python la variable create panna, just assign value:'''


'''
x = 10
name = "Sri macha"
pi = 3.14'''


#==============================================================#

# 2. Naming Rules for Variables

'''
| Rule                      | Example         |
| ------------------------- | --------------- |
| Must start with letter/\_ | `x`, `_temp` ✅  |
| Can't start with number   | `1value` ❌      |
| No special chars          | `my-name` ❌     |
| Case sensitive            | `name` ≠ `Name` |

🧠 Good practice: use meaningful names like student_name, age, etc.

'''

#====================================================================#

# 3. Python Data Types

'''
| Type    | Example               | Description                      |
| ------- | --------------------- | -------------------------------- |
| `int`   | `10`, `-4`, `0`       | Integer values                   |
| `float` | `3.14`, `0.0`, `-9.8` | Decimal values                   |
| `str`   | `"Hello"`, `'Hi'`     | Text data (single/double quotes) |
| `bool`  | `True`, `False`       | Boolean values                   |
'''
#====================================================================#


# 4. Check Type using type() Function

'''a = 10
b = "Python"
print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>
'''


#====================================================================#

# 5. Type Casting(Convert from one type to another)

'''
| Function  | Converts to... |
| --------- | -------------- |
| `int()`   | Integer        |
| `float()` | Float          |
| `str()`   | String         |
| `bool()`  | Boolean        |
'''

#====================================================================#

#  6. Multiple Assignment

'''
x, y, z = 1, 2, 3

name = age = "Sri macha"  # same value to multiple variables'''

#====================================================================#


# 7. Swap Variables (Python magic!)


'''
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10'''


#====================================================================#

# Practice Time!


#Store your name, age, and height in variables.

name = 'sridhar'
age = 13
height = 1.90
print(name, age, height)



#====================================================================#

# Convert an integer to string and print its type.

number = 23

total = str(number)

print(type(total))


# Swap two numbers using Python shortcut.


a,b = 10,20
a,b = b,a
print(a,b)






