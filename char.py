X = input().strip()
if 'a' <= X <= 'z':
        print(chr(ord(X) - 32))
else:
    print(chr(ord(X) + 32))
