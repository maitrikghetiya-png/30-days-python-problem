# Q1. Write a Python program using nested if statements to check admission eligibility
# based on marks (at least 60) and age (at least 18). Print an appropriate message 
# and test with two inputs.

mark=float(input("enter your mark:-"))
age=int(input("enter your age:-"))
if mark>=60:
    if age>=18:
        print("Admission Apporved")
    else:
        print("your age is minor")
else:
    print("Admission not Apporved because your mark is not greater equel 60")
# # q.2 Basic + Challenging: Smart Transaction Validator
# Write a Python program that accepts a bank balance and a withdrawal amount.
# Requirements:
# Check whether the withdrawal amount is positive.
# Check whether the amount is a multiple of ₹100.
# Check whether the account has sufficient balance.
# Print "Transaction Successful" only if all three conditions are satisfied.
# Otherwise, print the appropriate reason for rejection.
# Restriction: Use only if statements and logical operators. Do not use elif or else.

amount = int(input("enter your amount: "))
balance = int(input("enter the balance: "))

if amount <= 0:
    print("Withdrawal amount must be positive")

if amount % 100 != 0:
    print("Amount must be a multiple of ₹100")

if amount > balance:
    print("Insufficient balance")

if amount > 0 and amount % 100 == 0 and amount <= balance:
    print("Transaction Successful")

# q.3Write a Python program that accepts an employee's c, years of experience, performance rating (out of 10), and attendance percentage.
# Requirements.
# Print "Bonus Eligible" if experience is at least 3 years, rating is at least 8, and attendance is at least 90%.
# Print "Promotion Eligible" if experience is at least 5 years and rating is at least 9.
# Print "High Performer" if the rating is at least 9, regardless of the other conditions.
# Each result must be checked independently.
# If the salary is greater than ₹1,000,000, print "High Salary Band".
# Restriction: Use independent if statements with appropriate logical operators. Multiple messages may appear.

salary=int(input("enter your salary:-"))
experience=float("enter your experience:-")
rating=int(input("(out of ten)rating:-"))
att_per=int("attendance percentage:-")
if rating>=9:
    print("High Performer")
if experience>=3 and rating>=8 and att_per>=90:
    print("Bonus Eligible")
else:
    print("Bonus not Eligiable")

if experience>=5 and rating>=9:
    print("Promotion Eligible")
else:
    print("Promotion not Eligible")
if salary>1000000:
    print("High Salary Band")

# Q3. Expert Level: Nested if Admission and Scholarship System
# Write a Python program for a college admission system using nested if statements only
# Accept these inputs:
# Student age
# Entrance exam score (out of 100)
# . Class 12 percentage
# Family annual income
# I
# Requirements:
# 1. Check whether the student is at least 18 years old.
# 2. If eligible by age, check whether the entrance score is at least 75.
# 3. If the entrance score qualifies, check whether the Class 12 percentage is at least 60.
# 4. If all admission requirements are satisfied, print "Admission Approved"
# 5. Inside the approved admission block, check whether the family income is at most *300,000 and the entrance score is at least 90.
# 6. If both scholarship conditions are satisfied, print "Full Scholarship Eligible"
# 7. Otherwise, if admission requirements fall, print the specific reason for rejection.
# Challenge: Design the nested conditions so the scholarship check runs only after admission is approved. Avoid elif, else, and compound shortcuts that replace the required nested structure.

student_age=int(input("enter your age:-"))
score=float(input("(out of100)enter the entrance score:-"))
per=float(input("enter your class 12 percentage:-"))
income=float(input("enter your annual income:-"))
if student_age<18:
    print("age is not elgiable")
if score<75:
    print("score is not greater than equal 75")
if per<60:
    print("percentage is not enough")
    
if student_age>=18:
    if score>=75:
        if per>=60:
            print("Admission Approved")
            if income<=3000000 and score>=90:
                print("Full Scholarship Eligible")

