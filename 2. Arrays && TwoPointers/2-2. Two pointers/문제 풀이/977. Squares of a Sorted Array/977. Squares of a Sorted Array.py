def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    result = [0] * len(nums)
    n = len(nums) - 1

    while left <= right:
        left_nums = nums[left] ** 2
        right_nums = nums[right] ** 2
        if left_nums <= right_nums:
            result[n] = right_nums
            right -= 1
        if left_nums > right_nums:
            result[n] = left_nums
            left += 1
        n -= 1
    return result


nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))
