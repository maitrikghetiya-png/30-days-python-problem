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

