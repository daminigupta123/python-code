n, m = map(int, input().split())
arr = list(map(int, input().split()))

freq = [0] * (m + 1)

for num in arr:
    freq[num] += 1

for i in range(1, m + 1):
    print(freq[i])
