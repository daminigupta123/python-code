N = int(input())
A = list(map(int, input().split()))
X = int(input())
pos = -1
for i in range(N):
    if A[i] == X:
        pos = i
        break
print(pos)
