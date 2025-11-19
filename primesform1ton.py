N = int(input())
def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True
for num in range(2, N + 1):
    if is_prime(num):
        print(num, end=" ")
