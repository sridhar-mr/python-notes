#MODES (ONE LINE SUMMARY)

# 'r' ---> READE ONLY (FILE MUST EXIST)
# 'w' ---> WRITE ONLY (OVER WRITE OR CREATE)
# 'a' ---> APPEND ONLY (ADD TO END OF FILE)
# 'r+' ---> READ + WRITE (FILE MUST EXIST)
# 'w+' ---> WRITE + READ  (OVER WRITE OR CREATE)
# 'a+' ---> APPEND + READ  (CREATE IF NOT EXIST)
# 'rb' ---> READ BINARY
# 'wb' ---> WRITE BINARY
# 'ab' ---> APPEND BINARY



#this was write --> w
f = open("file-handling.txt", "w")
f.write("I create a file using write and add the text\n") #\n beark a line
f.close()


#this was read  --> r
f = open("file-handling.txt", 'r')
content = f.read()  # it was small content we can use this read()
print("File content: ", content)
f.close()


#this was append --> a
f = open("file-handling.txt", 'a')
f.write("Adding Append Line ")
f.close()



#with block


with open("file-handling.txt", "r") as file:  #we can't use a close it will close automatically
    for line in file:
        print(line.strip())


# login feedback


feedback = input("Tell Me a Feedback about our product: ")

with open("file-handling.txt", 'a') as log:
    log.write( "\n" + "Login Feedback --- " +  feedback)

print("Thank You For your Feedback 💕 ")


#readline() --> we can use this large file

with open("file-handling.txt", "r") as file:
   print( file.readline().strip())


#find a line or word
with open("file-handling.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        if "add" in line:
            print("FOUND A WORD: ", line)



#using for loop  i need a particular line

with open("file-handling.txt", 'r') as file:
    for _ in range(2):   #_ this means throe away variable that particular place what ever value come also no need
        print(file.readline().strip())



# one file to another file add

with open("file-handling.txt", 'r') as infile, open("file-output.txt", 'w') as outfile:
    for line in infile:
        print(line.strip())
        outfile.write(line)



# particular data take

import csv

with open("file_csv.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["age"])