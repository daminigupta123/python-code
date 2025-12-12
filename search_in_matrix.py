
# N, M = map(int, input().split())

# found = False

# for _ in range(N):
#     row = list(map(int, input().split()))
#     if X in row:
#         found = True

# X = int(input())


# if found:
#     print("will not take number")
# else:
#     print("will take number")
# Read N and M
N, M = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
X = int(input())
found = False
for row in matrix:
    if X in row:
        found = True
        break
if found:
    print("will not take number")
else:
    print("will take number")
