nums = [-10, 34, 98, 12, -12, -345]
nums2 = []

for num in nums:
    nums2.append(abs(num))
    # if num < 0:
    #     nums2.append(num * -1)
    # else:
    #     nums2.append(num)

print(nums2) # Output: [10, 34, 98, 12, 12, 345]