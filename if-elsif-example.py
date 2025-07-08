# Check if a number is positive or negative

userinput = int(input("Enter the Number: "))

if userinput > 0:
  print("Positive Number")
else:
  print("Negative Number")


#=============================#

 #Check if a number is even or odd

userNumber =  int(input("Enter your Number: "))

if userNumber%2==0:
  print("Even Number")
else:
  print("Odd Number")





# Check if a person is eligible to vote (age >= 18)


userage = int(input("Enter Your Age: "))

if userage >= 18:
    print("Eligiable to Vote")
else:
    print("Not Eligiable to vote")


#  Check if a year is a leap year or not

userYear = int(input("Enter the Year: "))

if userYear%40==0:
  print("Leap Year")
else:
  print("Not a Leap Year")




# Find the biggest of two numbers

user1 = int(input("Enter one number"))
user2 = int(input("Enter again one number"))


if user1 > user2:
  print("Biggest Number: ")
else:
  print("Smallest Number: ")




  #Check if a given character is a vowel or not

userVowel = input("Enter the words") #-> signle words

if userVowel.lower() in "aeiou":
  print("Its a Vowel")
else:
  print("its not vowel")


  #Check if a given number is a multiple of 3 and 5

usermultiple = int(input("Enter The  Number: "))

if usermultiple%3==0 and usermultiple%5==0:
  print("Multiple by 3 and 5")
else:
  print("Not Multiple by 3 and 5")


  # Check if a person’s name is "Sridhar" → If yes, say "VIP Entry", else "Normal Entry"


name = "sridhar"

if name == "sridhar":
  print("VIP Entery")
else:
  print("Normal Entry")


#===================================================================================#

#=========================== LEVEL 2==================#


""""
 Mark Grade Calculator
👉 Input: Student’s mark
👉 Output:

If mark >= 90 → "Distinction"

If mark >= 60 → "Pass"

Else → "Fail"

🧠 Bonus: Handle invalid mark (like >100 or <0)
"""


studentMark = int(input("Enter Your Mark: "))


if studentMark >= 90:
  print("Distinction")
elif studentMark >= 60:
  print("Pass")
else:
  print("Fail")


  #+======================================================#

  """
  2️⃣ Biggest of Three Numbers
👉 Input: 3 numbers
👉 Output: Print the largest one
(Use if-elif-else logic)
  """

biggestNumber1 = int(input("Enter The first Number: "))
biggestNumber2 = int(input("Enter The second Number: "))
biggestNumber3 = int(input("Enter The Third Number: "))


if biggestNumber1 > biggestNumber2 and biggestNumber1 > biggestNumber3:
  print(biggestNumber1)
elif biggestNumber2 > biggestNumber3 and biggestNumber2 > biggestNumber1:
  print(biggestNumber2)
else:
  print(biggestNumber3)

  #=========================================#
  """
  3️⃣ Check Leap Year
👉 Input: A year (e.g. 2024)
👉 Output: Whether it’s a leap year or not


Leap year logic:
- Divisible by 4 ✅
- But if divisible by 100 ❌
- Unless also divisible by 400 ✅
  """


year = int(input("Enter any Year: "))

if year % 400 == 0:
    print("It's a Leap Year")
elif year % 100 == 0:
    print("It's NOT a Leap Year")
elif year % 4 == 0:
    print("It's a Leap Year")
else:
    print("It's NOT a Leap Year")


#=================================================#


"""
4️⃣ ATM Withdrawal Logic
👉 Input: Your bank balance and withdrawal amount
👉 Output:

If withdrawal <= balance → "Transaction Successful"

Else → "Insufficient Balance"

💡 Bonus: Add condition → withdrawal should be multiple of 100
"""


accountBalance = 10000
withdrawalAmount = int(input("Enter Your Withdraw Amount"))


if withdrawalAmount <= accountBalance:
        total = accountBalance-withdrawalAmount
        print("Transaction Successful", total , "Avaliable ")
                  
else:
  print("Insufficient Balance")




  #====================================================================#


  '''
  5️⃣ Time-Based Greeting
👉 Input: Hour (0 to 23)

Output:

0–11: "Good Morning"

12–16: "Good Afternoon"

17–20: "Good Evening"

21–23: "Good Night"

Else: "Invalid hour"
  '''



hour = int(input("Enter the Hours between 0 - 23 "))

if 0 <= hour <= 11:
    print("☀️ Good Morning!")
elif 12 <= hour <= 16:
    print("🌤️ Good Afternoon!")
elif 17 <= hour <= 20:
    print("🌇 Good Evening!")
elif 21 <= hour <= 23:
    print("🌙 Good Night!")
else:
    print("❌ Invalid hour. Please enter between 0 and 23.")





    #=====================================LEVEL 3 =========================#


    '''
    1️⃣ Electricity Bill Calculator ⚡
Input: Total units used
Output: Final bill amount with slab rates

Units Range	Price per Unit
0–100	₹1.5
101–200	₹2.5
201–300	₹4
301+	₹6

👉 Example: 350 units = 100×1.5 + 100×2.5 + 100×4 + 50×6
    
    '''
units = int(input("Enter your unit consumption: "))

if units < 0:
    print("Invalid value")
elif units <= 100:
    total = units * 1.5
elif units <= 200:
    total = (100 * 1.5) + ((units - 100) * 2.5)
elif units <= 300:
    total = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)
else:
    total = (100 * 1.5) + (100 * 2.5) + (100 * 4) + ((units - 300) * 6)

print("Total Bill Amount is ₹", total)



#=======================================================================#





'''
Student Result Sheet 
Input: 3 subject marks
Output:

If any subject < 35 → Fail

Else → check total & give:

90+ avg → "Distinction"

60+ avg → "First Class"

40+ avg → "Pass"

Bonus: Show Total & Average too
'''


sub1 = int(input("Enter your Math mark: "))
sub2 = int(input("Enter your Chemistry mark: "))
sub3 = int(input("Enter your Physics mark: "))

if sub1 < 35 or sub2 < 35 or sub3 < 35:
    print("❌ Result: FAIL (One or more subjects below 35)")
else:
    total = sub1 + sub2 + sub3
    average = total / 3

    print("✅ Total Marks:", total)
    print("📊 Average:", average)

    if average >= 90:
        print("🏆 Grade: Distinction")
    elif average >= 60:
        print("🥇 Grade: First Class")
    elif average >= 40:
        print("✅ Grade: Pass")
    else:
        print("❌ Grade: Fail")



#==================================================#




