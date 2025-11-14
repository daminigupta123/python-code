n = input().strip()
if '.' in n:
    integer, decimal = n.split('.')
    if int(decimal) == 0:    
        print("int", integer)
    else:
        print("float", integer, "0." + decimal)
else:
    print("int", n)
