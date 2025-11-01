def reverse_number(n):
       return int(str(n)[::-1])
N = int(input().strip())
for _ in range(N):
    line = input().strip().split()
    a = int(line[0])
    b = int(line[1])
    result = reverse_number(reverse_number(a) + reverse_number(b))
    print(result)