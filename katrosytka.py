n, m, k = map(int, input().split())
canditionA = min(k, m, n)
canditionB = min(k, (n + m) // 2)
answer = canditionA
if canditionB > m:
    answer = max(answer, canditionB)
print(answer)
