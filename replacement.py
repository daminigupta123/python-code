N = int(input())
A = list(map(int, input().split()))
result = []
for x in A:
    if x > 0:
        result.append(1)
    elif x < 0:
        result.append(2)
    else:
        result.append(0)

print(*result)
