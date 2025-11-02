def best_package_size(N):
    return (N // 2) + 1
T = int(input())  
for _ in range(T):
    N = int(input())
    print(best_package_size(N))
