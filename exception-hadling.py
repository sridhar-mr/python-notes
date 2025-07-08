from xml.etree.ElementTree import indent

from win32com.servers import dictionary

try:
    number_of_items = int(input("How many items do you have?: "))
    tota_price = 200 *  number_of_items
    avarage_price = tota_price/number_of_items
except ZeroDivisionError:   #--> what error do know ,eans we can use Exception   
    print("You cannot order 0 items")



# what are the error

# ZeroDivisionError --> dividing a number by zer0 10/0

# ValueError --> invalid value for a fuction (e.g int("abc"))

# TypeError --> wrong data type used in operation  "abc" + 10

# IndexError --> Accessing out-of-range list in index my_list[10]

# KeyError  ---> Accessing a non-existing key in a dictionary  my_dict["not_found"]

# AttributeError --> accessing a non-exsiting attribute of an object None.upper()

# FileNotFoundError ---> file not found when opening open("abc.txt")

# ImportError --> trying to import missing module import notamodule

# NameError ---> using a variable that was never defined print(xyz)

# IndentationError ---> incorrect indentattion code not properly indent

# SyntaxError ---> Writing invalid python  code if true print("hi")

# RuntimeError ---> generic error not falling into other categories rare case

# StopIteration --> raised my next() when iteration is exhausted in loops and generators

# MemoryError ---> Programs runs out of memory working with huge data

# RecursionError ---> Too many recursive calls  A function calls itself endlessly

