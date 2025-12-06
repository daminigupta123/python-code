t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    best_left = arr[0] - 1          
    ans = float('inf')
    for j in range(1, n):          
        current = arr[j] + (j + 1) 
        ans = min(ans, best_left + current)
        best_left = min(best_left, arr[j] - (j + 1))
    print(ans)
