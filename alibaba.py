
a, b, c, d = map(int, input().split())

ops = ['+', '-', '*']

def eval_three(a, op1, b, op2, c):
    
    if op2 == '*' and op1 != '*':
        
        right = b * c
        if op1 == '+':
            return a + right
        else:  
            return a - right
    elif op1 == '*' and op2 != '*':
        
        left = a * b
        if op2 == '+':
            return left + c
        else: 
            return left - c
    elif op1 == '*' and op2 == '*':
        
        return (a * b) * c
    else:
        
        tmp = a + b if op1 == '+' else a - b
        return tmp + c if op2 == '+' else tmp - c

found = False
for op1 in ops:
    for op2 in ops:
        if eval_three(a, op1, b, op2, c) == d:
            found = True
            break
    if found:
        break

print("YES" if found else "NO")
