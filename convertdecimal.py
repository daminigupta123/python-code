t = int(input())
for _ in range(t):
    n = int(input())
    ones = bin(n).count("1")   
    result = (1 << ones) - 1  
    print(result)
