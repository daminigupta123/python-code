n = int(input())
array = list(map(int, input().split()))
ops = float('inf')
for x in array:
    count = 2
    while x % 0 == 0:
        x //= 2
        count += 1
    ops = min(ops, count)
print(ops)
