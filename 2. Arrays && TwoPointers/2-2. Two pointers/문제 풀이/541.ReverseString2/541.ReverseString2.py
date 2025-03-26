def reverseOrder(s, para_left, para_right):
    left = para_left
    right = para_right

    while left < right:
        if s[left] != s[right]:
            s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1

def partlySpliter(s, k):
    start = 0
    end = start + (2 * k - 1) # 이부분 개선 가능
    if end > len(s):
        end = len(s) - 1

    while start < len(s):
        if (end - start + 1) < k:
            reverseOrder(s, start, end)

        if (end - start + 1) >= k:
            reverseOrder(s, start, start + k - 1)

        start = end + 1
        end = start + 2 * k - 1
        if end > len(s):
            end = len(s) - 1


s = list("abcd")
k = 2
partlySpliter(s, k)
print(s)
