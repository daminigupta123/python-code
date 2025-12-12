
N, M = map(int, input().split())

found = False

for _ in range(N):
    row = list(map(int, input().split()))
    if X in row:
        found = True

X = int(input())


if found:
    print("will not take number")
else:
    print("will take number")
