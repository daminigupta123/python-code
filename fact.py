
def factorial(n):
    if n < 0:
        raise ValueError("not valid number")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Factorial of {n} is {factorial(n)}")
