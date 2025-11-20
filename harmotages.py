S = input().strip()
N = int(input())
numbers = list(map(int, input().split()))
for x in numbers:
    print(S * x)
