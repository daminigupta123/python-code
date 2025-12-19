a = int(input())
n = list(map(int, input().split()))
s = set(n)
count = 0

for x in a:
    if x + 1 in s:
        count += 1

print(count)
