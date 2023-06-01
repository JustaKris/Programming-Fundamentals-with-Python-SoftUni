nums = input().split(", ")

nums = [int(x) for x in nums]
zeroes = nums.count(0)
for i in range(zeroes):
    nums.remove(0)
for i in range(zeroes):
    nums.append(0)
print(nums)

# ChatGPT solution
# num_list = [int(num) for num in nums.split(", ")]
# zeros = [num for num in num_list if num == 0]
# non_zeros = [num for num in num_list if num != 0]
# result = non_zeros + zeros
# print(result)
