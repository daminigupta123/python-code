A, m = map(int, input().split())
for _ in range(A):
    row = list(map(int, input().split()))
    for x in row[::-1]:
        print(x, end=" ")
    print()
n = int(input())