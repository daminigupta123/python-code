N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    min_index = i
    for j in range(i + 1, N):
        if A[j] < A[min_index]:
            min_index = j
    A[i], A[min_index] = A[min_index], A[i]
for x in A:
    print(x, end=" ")
