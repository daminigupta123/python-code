N, K = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(0, N, K):
    group = arr[i:i+K]
    print(min(group), end=" ")
