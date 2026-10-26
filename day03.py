# Write a program that examines every pair of integers 1 and j
# Skip pairs where i == j.
# Skip pairs where both numbers are even.
# Stop the inner loop when i * j > 100
# Print only pairs whose sum is a prime number.
# Count and display the total number of pairs printed.
# from 1 to 20, subject to these rules:
# Use nested loops and conditional statements to solve the problem
        
count = 0

for i in range(1, 21):
    for j in range(1, 21):
        if i == j or (i % 2 == 0 and j % 2 == 0):
            continue

        if i * j > 100:
            break

        s = i + j
        if s > 1 and all(s % k != 0 for k in range(2, s)):
            print(i, j)
            count += 1

print("Total pairs:", count)
            
# '''digit pattem
# print all num from 100 to 999 whose digit are strictly incresing from left to right and whose digit
# sum is divide by 3'''


for i in range(100, 1000):

    s = str(i)
    a, b, c = int(s[0]), int(s[1]), int(s[2])
    if a < b < c and (a + b + c) % 3 == 0:
        print(i, end=" ")
