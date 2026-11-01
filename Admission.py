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
