N = int(input())
for i in range(N):
    row = ""
    for j in range(N):
        if i == j and i == N//2:
            row += "X"
        elif i == j:
            row += "\\"
        elif i + j == N - 1:
            row += "/"
        else:
            row += "*"
    print(row)
