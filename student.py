# """ Write a function that receives a list of student records,where
# each record contains a student's name and a list of marks. In one
# pass through the records, determine the student with the highest average,
# count how many students passed every subject, and calculate the class-wide average of all
# individuls marks. Handle empty reords and students with no marks without crashing."""


students = [
    ("maitrik", [80, 90, 70]),
    ("Rahul", [60, 50, 40]),
    ("Priya", [90, 95, 85]),
    ("pratyush", [90, 76, 65]),
    ("shubham", [80, 96, 95]),
    ("Aman", [30,56,89])
]

top = None
highest_average = None
passed = 0
total_marks = 0
total_subjects = 0

for name, marks in students:

    if not marks:
        continue

    avg = sum(marks) / len(marks)

    if highest_average is None or avg > highest_average:
        highest_average = avg
        top = name

    total_marks += sum(marks)
    total_subjects += len(marks)

    if all(mark >= 40 for mark in marks):
        passed += 1

if total_subjects > 0:
    class_average = total_marks / total_subjects
else:
    class_average = 0


print("Top Student:", top)
print("Highest Average:", highest_average)
print("Students Passed:", passed)
print("Class Average:", round(class_average, 2))
