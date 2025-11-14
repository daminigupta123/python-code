A, B, C = map(int, input().split())
o1, o2, o3 = A, B, C
s1 = min(A, B, C)
s3 = max(A, B, C)
s2 = A + B + C - s1 - s3  
print(s1)
print(s2)
print(s3)
print()
print(o1)
print(o2)
print(o3)
