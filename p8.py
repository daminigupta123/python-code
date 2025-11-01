def last_digit_power(a, b):
    if b == 0:
        return 1
    
    # Get last digit of base
    a = a % 10
    
    # Find pattern of last digits
    pattern = []
    temp = a
    while True:
        if temp not in pattern:
            pattern.append(temp)
        else:
            break
        temp = (temp * a) % 10
    
    # Use pattern length to find last digit
    pattern_length = len(pattern)
    index = (b - 1) % pattern_length
    return pattern[index]

# Read number of test cases
N = int(input())

# Process each test case
for _ in range(N):
    a, b = map(int, input().split())
    result = last_digit_power(a, b)
    print(result)