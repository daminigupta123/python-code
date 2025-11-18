def print_nums(n):
    if n == 0:
        return
    print_nums(n - 1)
    print(n)
N = int(input())
print_nums(N)
