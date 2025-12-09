t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    counting = 1    
    total_ans  = 0
    for i in range(1, n):
        if array[i] >= array[i-1]:
            counting += 1
        else:
            total_ans += counting * (counting + 1) // 2
            counting = 1            
    
    total_ans += counting * (counting + 1) // 2
    
    print(total_ans)
