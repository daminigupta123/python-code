# Function 
def last_stone(N):
 
    
    while N > 0:
    
        if N - i <= 0:
            return "Ramesh"
        N -= i
        
      
        if N - i * 2 <= 0:
            return "Suresh"
        N -= i * 2
        
        i += 1 
    

N = int(input().strip())

print(last_stone(N))
