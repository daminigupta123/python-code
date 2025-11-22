T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    a, b = min(X, Y), max(X, Y)
    final = 0
    for n in range(a + 1, b):
        if n % 2 != 0:
            final += n
    print(final)