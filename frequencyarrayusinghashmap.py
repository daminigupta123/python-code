n, m = map(int, input().split())
arr = list(map(int, input().split()))
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1

for i in range(1, m + 1):
    print(freq.get(i, 0))
