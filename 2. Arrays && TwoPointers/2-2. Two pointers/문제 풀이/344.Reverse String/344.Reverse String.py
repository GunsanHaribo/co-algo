def reverseString(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1


s = ["h","e","l","l","o"]
reverseString(s)

print(s)
