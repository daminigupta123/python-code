import math
def solve():
    n, k, a = map(int, input().split())
    INT_MIN, INT_MAX = -2147483648, 2147483647
    LL_MIN, LL_MAX = -2**63, 2**63 - 1
    value = n * math.pow(k, a)
    if value.is_integer():
        value = int(value)
        if INT_MIN <= value <= INT_MAX:
            print("int")
        elif LL_MIN <= value <= LL_MAX:
            print("long long")
        else:
            print("double")
    else:
        print("double")
