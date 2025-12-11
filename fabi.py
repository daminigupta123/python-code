t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    count = 1     
    total = 0
    
    for i in range(1, n):
        if arr[i] >= arr[i-1]:   
            count += 1
        else:
            total += count * (count + 1) // 2
            count = 1           
    
    
    total += count * (count + 1) // 2
    
    print(total)
