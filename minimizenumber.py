n = int(input())
arr = list(map(int, input().split()))
ops = float('inf')
for x in arr:
    count = 0
    while x % 2 == 0:
        x //= 2
        count += 1
    ops = min(ops, count)
print(ops)
