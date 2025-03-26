def reverseOrder(s, left, right):
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

def partlySpliter(s, k):
    start = 0
    n = len(s)

    while start < n:
        end = min(start + k - 1, n - 1)  # 범위를 벗어나지 않도록 조정
        reverseOrder(s, start, end)

        start += 2 * k  # 다음 2k 블록으로 이동

s = list("abcdefg")
k = 2
partlySpliter(s, k)
print("".join(s))  # 예상 출력: "bacd"