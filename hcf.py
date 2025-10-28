# # find out hcf of two numbers

def hcf(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
if __name__ == "__main__":
    x = int(input("first number: "))
    y = int(input(" second number: "))
    print(f"HCF  {x} and {y} is {hcf(x, y)}")
