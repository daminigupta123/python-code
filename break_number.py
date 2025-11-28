n = int(input())
arr = list(map(int, input().split()))
def f(x):
    cnt = 0
    while x % 2 == 0:
        x //= 2
        cnt += 1
    return cnt
ans = 0
for x in arr:
    ans = max(ans, f(x))
print(ans)
