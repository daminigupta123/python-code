n = int(input())
arr = list(map(int, input().split()))
l, r = 0, n - 1
result = []

while l <= r:
    result.append(arr[l])
    l += 1
    
    if l <= r:
        result.append(arr[r])
        r -= 1

print(*result)
