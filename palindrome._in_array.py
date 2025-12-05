N = int(input())
A = list(map(int, input().split()))
is_pal = True
for i in range(N // 2):
    if A[i] != A[N - 1 - i]:
        is_pal = False
        break
if is_pal:
    print("YES")
else:
    print("NO")
