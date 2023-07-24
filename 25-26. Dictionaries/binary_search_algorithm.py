def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle_index = (left + right) // 2
        middle_element = nums[middle_index]

        if middle_element == target:
            return middle_index

        if target > middle_element:
            left = middle_index + 1
        else:
            right = middle_index - 1


nums = [int(x) for x in input(" Numbers list: ").split()]
target = int(input("Target number: "))
print(f"Element is at index: {binary_search(nums, target)}")

# Example inputs
'''
1 2 Practice exam 1 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
7
'''
