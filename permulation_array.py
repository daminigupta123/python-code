from collections import Counter
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if Counter(A) == Counter(B):
    print("yes")
else:
    print("no")
