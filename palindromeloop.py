N = int(input())
curr= N
rev = 0
while curr > 0:
    rev = rev * 10 + curr % 10
    curr //= 10
print(rev)
if rev == N:
    print("YES")
else:
    print("NO")
