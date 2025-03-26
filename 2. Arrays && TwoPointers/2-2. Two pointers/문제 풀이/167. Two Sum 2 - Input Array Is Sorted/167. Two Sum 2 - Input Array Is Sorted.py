def twoSum(numbers, target):
    index1 = 0
    index2 = len(numbers) - 1
    while index1 < index2:
        if numbers[index1] + numbers[index2] == target:
            break
        if numbers[index1] + numbers[index2] < target:
            index1 += 1
        if numbers[index1] + numbers[index2] > target:
            index2 -= 1

    return [index1+1, index2+1]

numbers = [2,7,11,15]
target = 9

print(twoSum(numbers, target))