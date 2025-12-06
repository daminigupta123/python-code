n = int(input())
arr = list(map(int, input().split()))
minimum = arr[0]
for x in arr:
    if x < minimum:
        minimum = x
freq = 0
for x in arr:
    if x == minimum:
        freq += 1
if freq % 2 == 1:
    print("Lucky")
else:
    print("Unlucky")
