T = int(input())
for _ in range(T):
    N = int(input())
    if N == 0:            
        print(0)
        continue
    answer = []
    while N > 0:
        answer.append(N % 10)
        N //= 10           
    print(*answer)