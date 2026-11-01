# Advance Question 1:

# #Given a list of integers, find the second-largest DISTINCT value

# without sorting the list and without using max(), min(), or set().

# If fewer than two distinct values exist, return None.
nums = [12, 34, 34, 56, 78,78, 10]
first = None
second = None

for num in nums:
    if num == first:
        continue

    if first is None or num > first:
        second = first
        first = num

    elif second is None or num > second:
        second = num

print("First largest:", first)
print("Second largest:", second)
