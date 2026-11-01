# # q.2 Basic + Challenging: Smart Transaction Validator
# Write a Python program that accepts a bank balance and a withdrawal amount.
# Requirements:
# Check whether the withdrawal amount is positive.
# Check whether the amount is a multiple of ₹100.
# Check whether the account has sufficient balance.
# Print "Transaction Successful" only if all three conditions are satisfied.
# Otherwise, print the appropriate reason for rejection.
# Restriction: Use only if statements and logical operators. Do not use elif or else.

amount = float(input("enter your amount: "))
balance = float(input("enter the balance: "))

if amount <= 0:
    print("Withdrawal amount must be positive")

if amount % 100 != 0:
    print("Amount must be a multiple of ₹100")

if amount > balance:
    print("Insufficient balance")

if amount > 0 and amount % 100 == 0 and amount <= balance:
    print("Transaction Successful")
