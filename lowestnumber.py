n = int(input())
arr = list(map(int, input().split()))
min_val = min(arr)              
pos = arr.index(min_val) + 1    
print(min_val, pos)
