N = int(input())
A = list(map(int, input().split()))
mn = min(A)
mx = max(A)

min_index = A.index(mn)
max_index = A.index(mx)


A[min_index], A[max_index] = A[max_index], A[min_index]

print(*A)
