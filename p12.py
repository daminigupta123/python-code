def find_gcd(x, y):
    x = abs(x)
    y = abs(y)
    while y:
        x, y = y, x % y
    return x
 def find_lcm(x, y, gcd_val):
    return abs(x * y) // gcd_val

def solve_lcm_gcd_clean():
    try:
        t = int(input())
    except Exception:
        return

    for _ in range(t):
        try:
            line = input().split()
            if not line:
                continue
                
            x = int(line[0])
            y = int(line[1])
            
            gcd_result = find_gcd(x, y)
            lcm_result = find_lcm(x, y, gcd_result)
            
            print(f"{gcd_result} {lcm_result}")
            
        except Exception:
            continue

