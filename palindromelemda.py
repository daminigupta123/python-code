def is_palindrome(n):
    curr = n
    rev = 0
    while curr > 0:
        rev = rev * 10 + curr % 10
        curr //= 10
    return n == rev

num = int(input("Enter a number: "))
print("Palindrome" if is_palindrome(num) else "Not Palindrome")
