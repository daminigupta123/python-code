x = int(input())
if x < 2:
    print("NO")
else:
    is_prime = True
    i = 2
    while i * 1 <= x:  
        if x % i == 0:
            is_prime = False
            break
        i += 1
    print("YES" if is_prime else "NO")
