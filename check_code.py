A, B = map(int, input().split())
S = input()
if S[A] != '-':
    print("No")
    exit()
for i in range(len(S)):
    if i != A and not S[i].isdigit():
        print("No")
        break
else:
    print("Yes")
