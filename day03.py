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
            
