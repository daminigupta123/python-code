K, S = map(int, input().split())
ans = 0
for x in range(0, K+1):
    T = S - x
    low = max(0, T - K)
    high = min(K, T)
    if low <= high:
        ans += (high - low + 1)
print(ans)
