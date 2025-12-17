t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    if w == h:
        print("Square")
    else:
        print("Rectangle")
