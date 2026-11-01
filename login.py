# Question 5 Login Security with Multiple Conditions

# Build a login verification program.

# Rules:

# Username must be correct.

# Password must be correct.

# Account must be active.

# OTP must be correct.

# After three failed login attempts, lock the account.

# Tricky condition: The username and password are correct, but the account is inactive and the OTP is

# also incorrect.

# Task: Use nested conditions and logical operators to identify the exact failure reason. The program should stop authentication as soon as a required check fails.    


user="quad"
password="76890"
otp=2345

input_user=input("enter the user:-")
input_password=input("enter the password:-")
input_status="inactive"
input_attempts=2

if user==input_user and password==input_password:
    if input_status=="active":
        if input_attempts<4:
            input_otp=int(input("enter the otp:-"))
            if otp==input_otp:
                print("login successful")
            else:
                print("incorrect otp")
        else:
            print("attempts are more than 3.plz try later")
    else:
        print("account is inactive")
    
else:
    print("username or password  is incorrect")
