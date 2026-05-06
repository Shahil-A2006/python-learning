# 1. Merge Two Lists
# a = [1, 2, 3]
# b = [4, 5, 6]

# a.extend(b)
# print(a)


# 2. Find Maximum and Minimum
# nums = [10, 5, 20, 8]

# print("maximum value:",max(nums))
# print("minimum value:",min(nums))

# 3. Count Occurrences
# nums = [1, 2, 2, 3, 2, 4]
# print(nums.count(2))

# 4. Reverse a List (without reverse())
# nums = [1, 2, 3, 4]
# rev=[]

# for i in nums:
#     rev = [i] + rev

# print(rev)


# 5. Sum of All Elements
# nums = [5, 10, 15]

# print(sum(nums))

# Find the total sum using a loop

# nums = [5, 10, 15]

# total = 0
# for i in nums:
#     total = total + i

# print(total)

# 6. Find Even Numbers
# Create a new list with only even numbers
# nums = [1, 2, 3, 4, 5, 6]

# nums = [1, 2, 3, 4, 5, 6]
# even=[]

# for i in nums:
#     if i % 2 == 0:
#         even.append(i)

# print(even)


# 7. Remove Element
# nums = [10, 20, 30, 20, 40]
# Remove all occurrences of 20

# nums = [10, 20, 30, 20, 40]
# new = []

# for i in nums:
#     if i != 20:
#         new.append(i)

# print(new)


# 8. Find Index of Element
# nums = [5, 10, 15, 20]
# Find index of 15 without using index()

# nums = [5, 10, 15, 20]
# target = 15

# for i in range(len(nums)):
#     if nums[i] == target :
#         print(i)
#         break

# 9. Copy a List (without copy())
# nums = [1, 2, 3]
#  Create a copy manually

# nums = [1, 2, 3]
# new=[]

# for i in nums:
#     new.append(i)

# print(new)

# 10. Sort Without sort()
# nums = [4, 2, 1, 3]
#  Sort the list manually (hint: use loops)