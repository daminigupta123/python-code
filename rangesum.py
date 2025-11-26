def sum(n):
    return n * (n + 1) // 2
T = int(input())
for _ in range(T):
    L, R = map(int, input().split())
    print(sum(R) - sum(L - 1))
