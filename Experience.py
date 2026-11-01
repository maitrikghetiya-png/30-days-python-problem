# # Employee Bonus and Promotion

# # Determine an employee's bonus and promotion eligibility.

# # Rules:

# # Experience ≥ 10 years and rating ≥ 4.5: 25% bonus and promotion.

# # Experience ≥ 10 years and rating ≥ 3.5: 15% bonus, no promotion.

# # Experience ≥ 5 years and rating ≥ 4.0: 12% bonus.

# # Experience below 5 years and rating ≥ 4.5: 8% bonus.

# # All other cases: no bonus.

# # oal

# # Tricky condition: An employee has 12 years of experience but a rating of 3.2.

# # Task: Accept salary, experience, and rating; calculate the bonus amount and promotion status. Validate all inputs.


salary=int(input("enter the salary:-"))
exp=int(input("enter your experince in year:-"))
rating=float(input("enter rate (out of ten)"))

if exp>=10 and rating>=4.5:
    print("25% Bonus and promation")
    sal=salary*0.25+salary
    print("bonus:-",salary*0.25)
    print("bonus+salary:-",sal)
elif exp>=10 and rating>=3.5:
    print("15% Bonus and no promation")
    qwe=salary*0.15+salary
    print("bonus:-",salary*0.15)
    print("bonus+salary:-",qwe)
elif exp>=5 and rating>=4.0:
    print("12% Bonus")
    rty=salary*0.12+salary
    print("bonus:-",salary*0.12)
    print("bonus+salary:-",rty)
elif exp<5 and rating>=4.5:
    print("8% Bonus")
    yui=salary*0.08+salary
    print("bonus:-",salary*0.08)
    print("bonus+salary:-")
else:
    print("no bonus")
