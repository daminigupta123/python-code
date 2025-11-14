expr = input().strip()
for op in ['+', '-', '*', '/']:
    if op in expr:
        A, B = expr.split(op)
        A = int(A)
        B = int(B)
       
    if op == '+':
            print(A + B)
    elif op == '-':
        print(A - B)
    elif op == '*':
        print(A * B)
    elif op == '/':
        print(A // B)  
    break