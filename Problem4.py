palindrome = 0
for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        product = i * j
        if product > palindrome:
            productAsString = str(i * j)
            if productAsString == productAsString[::-1]:
                palindrome = i * j
print(palindrome)
