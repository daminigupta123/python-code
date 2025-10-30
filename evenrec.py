def print_even(n):
    if n < 2:
        return
    print_even(n - 2)
    print(n)

if __name__ == "__main__":
    n = int(input("Enter a number: "))

    if n % 2 != 0:
        n -= 1
    print(f"Even numbers from 2 to {n}:")
    print_even(n)