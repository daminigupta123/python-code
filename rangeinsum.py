import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
arr = list(map(int, input().split()))
pref = [0] * (n + 1)
for i in range(n):
    pref[i + 1] = pref[i] + arr[i]
for _ in range(q):
    l, r = map(int, input().split())
    print(pref[r] - pref[l - 1])
