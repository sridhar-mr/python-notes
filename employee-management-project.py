# Simple Employee Management System
#
# Add employee details (name, ID, department, salary)
#
# Calculate if they are eligible for bonus
#
# Save to file
#
# View all employees
#
# Search by ID

print("🙏 Welcome to Employee Management System")


def show_menu():
    print("\n1 ---> Add employee details")
    print("2 ---> View all employees")
    print("3 ---> Search by ID")
    print("4 ---> Exit")


class Employee:
    def __init__(self, name, id, department, salary):
        self.name = name
        self.id = id
        self.department = department
        self.salary = salary
        self.bonus = self.check_bonus()

    def check_bonus(self):
        if self.salary >= 50000:
            return "Eligible for Bonus"
        else:
            return "Not Eligible"

    def display(self):
        print(
            f"{self.id} | {self.name} | {self.department} | ₹{self.salary} | Bonus -- {self.bonus}"
        )


def save_employee_details(emp):
    with open("employee-details.txt", "a") as file:
        file.write(f"{emp.id},{emp.name},{emp.department},{emp.salary},{emp.bonus}\n")


def view_employee_details():
    try:
        with open("employee-details.txt", "r") as file:
            print("\n📃 Employee List:")
            for line in file:
                emp_data = line.strip().split(",")
                if len(emp_data) == 5:
                    print(
                        f"{emp_data[0]} | {emp_data[1]} | {emp_data[2]} | ₹{emp_data[3]} | Bonus -- {emp_data[4]}"
                    )
    except FileNotFoundError:
        print("❌ Employee file not found.")


def search_by_id(search_id):
    found = False
    try:
        with open("employee-details.txt", "r") as file:
            for line in file:
                emp_data = line.strip().split(",")
                if emp_data[0] == str(search_id):
                    print("\n🎯 Employee Found:")
                    print(f"ID: {emp_data[0]}")
                    print(f"Name: {emp_data[1]}")
                    print(f"Department: {emp_data[2]}")
                    print(f"Salary: ₹{emp_data[3]}")
                    print(f"Bonus Status: {emp_data[4]}")
                    found = True
                    break
        if not found:
            print("❌ Employee Not Found")
    except FileNotFoundError:
        print("❌ File not found.")


# 🔁 Main Loop
while True:
    show_menu()
    select = input("Select Number: ")

    if select == "1":
        name = input("Enter Name: ")
        emp_id = input("Enter Employee ID: ")
        dept = input("Enter Department: ")
        salary = int(input("Enter Salary: "))
        emp = Employee(name, emp_id, dept, salary)
        save_employee_details(emp)
        print("✅ Employee Saved!")

    elif select == "2":
        view_employee_details()

    elif select == "3":
        search_id = input("Enter Employee ID to search: ")
        search_by_id(search_id)

    elif select == "4":
        print("👋 Exiting. Thank you!")
        break

    else:
        print("❌ Invalid choice. Try again.")
