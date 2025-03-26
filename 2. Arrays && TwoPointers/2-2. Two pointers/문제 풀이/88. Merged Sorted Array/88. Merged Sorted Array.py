def merge(nums1, m, nums2, n):
    nums1_pointer = 0
    nums2_pointer = 0
    while nums1_pointer < m:
        if n == 0:
            nums1_pointer += 1
            continue

        if nums1[nums1_pointer] > nums2[nums2_pointer]:
            nums1[nums1_pointer], nums2[nums2_pointer] = nums2[nums2_pointer], nums1[nums1_pointer]
            nums2.sort()
        nums1_pointer += 1

    while nums2_pointer < n:
        nums1[nums1_pointer] = nums2[nums2_pointer]
        nums1_pointer += 1
        nums2_pointer += 1


nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
merge(nums1, m, nums2, n)
print(nums1)
