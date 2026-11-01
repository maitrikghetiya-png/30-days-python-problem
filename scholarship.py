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
