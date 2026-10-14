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

