import sys

input_data = sys.stdin.read().strip().split()
t = int(input_data[0])
idx = 1
out_lines = []

for _ in range(t):
    n = int(input_data[idx]); s = int(input_data[idx+1]); idx += 2
    maxsum = n*(n+1)//2
    if s > maxsum:
        out_lines.append("-1")
        continue

    ans = []
    # Greedy: take largest possible distinct numbers
    for i in range(n, 0, -1):
        if s >= i:
            ans.append(str(i))
            s -= i
        if s == 0:
            break

    # s should be 0 here
    out_lines.append(" ".join(ans))

print("\n".join(out_lines))
# print(column)
#from chatgpt