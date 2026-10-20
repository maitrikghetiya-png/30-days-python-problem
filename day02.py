# Question 1 Scholarship Eligibility Trap

# A college awards scholarships based on marks and family income.

# Rules:

# If any subject mark is below 35, the student fails.

# Otherwise, calculate the average of 3 subjects.

# Average ≥ 90 and income below ₹3,00,000: 100% scholarship.

# Average ≥ 80 and income below ₹5,00,000: 50% scholarship.

# Average ≥ 70: admission without scholarship.

# Otherwise: admission rejected.

# Tricky condition: A student scores 95, 96, and 30, with family income of ₹1,00,000. The average i high, but should the student receive a scholarship?

# Task: Write the complete program with input validation and nested conditions.


# 1. Take inputs with correct data types
mark1 = int(input("Enter your mark 1: "))
mark2 = int(input("Enter your mark 2: "))
mark3 = int(input("Enter your mark 3: "))
income = int(input("Enter the income: "))  # Converted to int to fix the crash

# 2. Validate marks range
if mark1 < 0 or mark1 > 100:
    print("Invalid mark 1")
elif mark2 < 0 or mark2 > 100:
    print("Invalid mark 2")
elif mark3 < 0 or mark3 > 100:
    print("Invalid mark 3")

# 3. Check for immediate failure
elif mark1 < 35 or mark2 < 35 or mark3 < 35:  # Changed to 'or' because failing ANY subject means fail
    print("Fail")

else:
    # 4. Calculate average correctly using parentheses
    avg = (mark1 + mark2 + mark3) / 3
    print("Average:", round(avg, 2))

    # 5. Scholarship & Admission Logic using clean if-elif blocks
    if avg >= 90:
        if income < 300000:  # Fixed income thresholds logically
            print("100 percentage scholarship.")
        elif income <= 500000:
            print("50% Scholarship.")
        else:
            print("Admission granted, but no scholarship.")
            
    elif avg >= 80:
        if income <= 500000:
            print("50% Scholarship.")
        else:
            print("Admission granted, but no scholarship.")
            
    elif avg >= 70:
        print("Admission without scholarship.")
        
    else:
        print("Admission rejected.")




# Create an ATM program with a balance of ₹15,000.

# Rules:

# Correct PIN: 4321.

# Withdrawal must be positive.

# The balance must never fall below ₹2,000.

# Withdrawals above ₹10,000 require manager approval.

# An incorrect PIN must prevent all further transactions.

# Tricky condition: The balance is 12,000 and the customer tries to withdraw ₹11,000 without manager approval.

# Task: Use nested if statements to handle every condition and display the correct remaining

# balance.

bal = 15000
cpin = 4321
min_bal = 2000

pin = int(input("Enter your PIN: "))
if pin == cpin:
    print("PIN is correct")
    amount = int(input("Enter withdrawal amount: "))
    if amount > 0:
        if (bal-amount)>=min_bal:
            if amount>10000:
                man=input("yes or no:-")
                if man=="yes":
                    print("amount withdrwal sucessful")
                else:
                    print("mag apporval requied")
            else:
                print("transiton sucessful")
        else:
            print("innsuisent balance")
    else:
        print("positive amount")
else:
    print("pin is not corret") 





# Question 3

# Triangle Classification Puzzle

# Accept three side lengths and classify the triangle.

# Rules:

# All sides must be positive.

# The sum of any two sides must exceed the third side.

# Classify it as equilateral, isosceles, or scalene.

# Also check whether it is right-angled using the Pythagorean theorem.

# Tricky condition: Inputs are 1, 2, 3. The sides look almost valid, but they do not form a triangle.

# Task: Reject invalid triangles before checking their type or angle.             
            
          
s1=int(input("enter side 1:-"))   
s2=int(input("enter side 2:-"))
s3=int(input("enter side 3:-"))
if s1>0 and s2>0 and s3>0:
    if s1+s2>s3 and s2+s3>s1 and s1+s3>s2:
        if s1**2+s2**2==s3**2 or s2**2+s3**2==s1**2 or s3**2+s1**2==s2**2:
            print("right angle triangle")
        if s1==s2==s3:
            print("equilateral")
        elif s1==s2 or s2==s3 or s1==s3:
            print("isosceles")
        else:
            print("scalene")
    else:
        print("side is not corret")        
else:
    print("negative side invaid") 


# # Employee Bonus and Promotion

# # Determine an employee's bonus and promotion eligibility.

# # Rules:

# # Experience ≥ 10 years and rating ≥ 4.5: 25% bonus and promotion.

# # Experience ≥ 10 years and rating ≥ 3.5: 15% bonus, no promotion.

# # Experience ≥ 5 years and rating ≥ 4.0: 12% bonus.

# # Experience below 5 years and rating ≥ 4.5: 8% bonus.

# # All other cases: no bonus.

# # oal

# # Tricky condition: An employee has 12 years of experience but a rating of 3.2.

# # Task: Accept salary, experience, and rating; calculate the bonus amount and promotion status. Validate all inputs.


exp=int(input("enter your experince in year:-"))
rating=float(input("enter rate (out of ten)"))

if exp>=10 and rating>=4.5:
    print("25% Bonus and promation")
elif exp>=10 and rating>=3.5:
    print("15% Bonus and no promation")
elif exp>=5 and rating>=4.0:
    print("12% Bonus")
elif exp<5 and rating>=4.5:
    print("8% Bonus")
else:
    print("no bonus")
