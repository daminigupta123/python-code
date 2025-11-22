N, A, B = map(int, input().split())
def digit_sum(x):
    return sum(int(d) for d in str(x))
total = 0
for num in range(1, N + 1):
    if A <= digit_sum(num) <= B:
        total += num
print(total)
