n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
max_sum = 0
for i in range(k):
    if a[i] > 0:
        max_sum += a[i]
print(max_sum)
