# # find out hcf of two numbers

def hcf(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
if __name__ == "__main__":
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"HCF of {x} and {y} is {hcf(x, y)}")
