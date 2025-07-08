

# Create a system to add, display, and search student records (Name, Roll No, 3 subject marks, total, grade) and save it to a file.

# '''
# ✅ Input
# ✅ Conditions
# ✅ Loops
# ✅ Functions
# ✅ File Handling
# ✅ OOP
# ✅ String handling
# ✅ Modules (optional split)


# '''

print("🎓 Welcome to Student Marks System 🎓")

def show_menu():
  print("Choose any one Option: ")
  print(" 1--> Add a Student")
  print(" 2--> View all Student")
  print(" 3--> Search by Roll Number")
  print(" 4--> Exit")



# using OOPS concept

class student:

  def __init__(self,name,roll_number,m1,m2,m3):

    self.name = name
    self.roll_number= roll_number
    self.m1 = m1
    self.m2 = m2
    self.m3 = m3
    self.total = m1+m2+m3
    self.grade = self.calculation_mark()
  


  def calculation_mark(self):
    avg = self.total/3
    if avg >= 90:
      return "Grade : A+"
    elif avg >= 75:
      return "Grade : A"
    elif avg >= 60:
      return "Grade : B"
    else:
      return "Grade : F"
  def display(self):
    print(f"{self.roll_number} - {self.name} - Total: {self.total} - Grade: {self.grade}")



  # save a data in text documents

  def save_studentdetails(student):
      with open("student_details.txt", "w") as file:
        file.write(f"{student.roll_number},{student.name}, {student.m1}, {student.m2} , {student.m3}. {student.total}, {student.grade}\n")



# View all Student details in txt
  def view_all_student():
      try:
        with open("student_details.txt", 'r') as file:
          for line in file:
            print(line().strip())
      except FileNotFoundError:
        print("No Student Records Founded")


# Roll Number Search
  def search_roll(rollno):
    found = False
    try:
      with open("student_details.txt", "r") as file:
        for line in file:
          data = line.strip().split(",")
          if data[0] == rollno:
              print("🎯 Student Found:")
              print("Roll Number: ", data[0])
              print("Student Name: ", data[1])
              print("3 Subject Marks: ", data[2], data[3], data[4])
              print("Total Marks: ", data[5], "Grade", data[6])
              found = True
              break
      if not found:
        print("Student Not Founded")
    except FileNotFoundError:
      print("File Not Founded")


# Full Loop Program


  while True:
    show_menu()
    select = int(input("Enter Your Choice:  "))
    if select == "1":
      name = input("Enter Your Name:  ")
      rollNumber = int(input(" Enter Your Roll Number: "))
      mark1 = int(input("Enter Your Mark 1: "))
      mark2 = int(input("Enter Your Mark 2: "))
      mark3 = int(input("Enter Your Mark 3: "))
      stu = student(name, rollNumber, mark1, mark2, mark3)
      save_studentdetails(stu)
      print("✅ Student saved successfully!")
    elif select == "2":
      view_all_student()
    elif select == "3":
      foundRollNumber = int(input("Enter Your RollNumber: "))
      search_roll(foundRollNumber)
    elif select =="4":
      print("👋 Thank you for using the system!")
      break
    else:
      print("❌ Invalid choice. Try again.")
    

