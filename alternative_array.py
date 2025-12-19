n = int(input())
a = list(map(int, input().split()))
flips1 = 0
flips2 = 0
for i in range(n):
    if i % 2 == 0:
            if a[i] < 0:
             flips1 += 1   
            if a[i] > 0:
             flips2 += 1  
    else:
        if a[i] > 0:
            flips1 += 1   
        if a[i] < 0:
            flips2 += 1 
print(min(flips1, flips2))
