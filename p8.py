import io, sys
sys.stdin = io.StringIO("2\n3 10\n6 2\n")
def last_digit_power(a, b):
    if b == 0:
     return 1
     a = a % 10
    pattern = []
    temp = a
    while True:
        if temp not in pattern:
            pattern.append(temp)
        else:
            break
    temp = (temp * a) % 10
    pattern_length = len(pattern)
    index = (b - 1) % pattern_length
    return pattern[index]
    N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    result = last_digit_power(a, b)
    print(result)