# q.3Write a Python program that accepts an employee's c, years of experience, performance rating (out of 10), and attendance percentage.
# Requirements.
# Print "Bonus Eligible" if experience is at least 3 years, rating is at least 8, and attendance is at least 90%.
# Print "Promotion Eligible" if experience is at least 5 years and rating is at least 9.
# Print "High Performer" if the rating is at least 9, regardless of the other conditions.
# Each result must be checked independently.
# If the salary is greater than ₹1,000,000, print "High Salary Band".
# Restriction: Use independent if statements with appropriate logical operators. Multiple messages may appear.

salary=float(input("enter your salary:-"))
experience=float("enter your experience:-")
rating=float(input("(out of ten)rating:-"))
att_per=float("attendance percentage:-")
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
