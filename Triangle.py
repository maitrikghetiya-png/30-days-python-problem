# Question 3

# Triangle Classification Puzzle

# Accept three side lengths and classify the triangle.

# Rules:

# All sides must be positive.

# The sum of any two sides must exceed the third side.

# Classify it as equilateral, isosceles, or scalene.

# Also check whether it is right-angled using the Pythagorean theorem.

# Tricky condition: Inputs are 1, 2, 3. The sides look almost valid, but they do not form a triangle.

# Task: Reject invalid triangles before checking their type or angle.             
            
          
s1=int(input("enter side 1:-"))   
s2=int(input("enter side 2:-"))
s3=int(input("enter side 3:-"))
if s1>0 and s2>0 and s3>0:
    if s1+s2>s3 and s2+s3>s1 and s1+s3>s2:
        if s1**2+s2**2==s3**2 or s2**2+s3**2==s1**2 or s3**2+s1**2==s2**2:
            print("right angle triangle")
        if s1==s2==s3:
            print("equilateral")
        elif s1==s2 or s2==s3 or s1==s3:
            print("isosceles")
        else:
            print("scalene")
    else:
        print("side is not corret")        
else:
    print("negative side invaid") 
