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
