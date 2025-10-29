def sum_natural(n):
    if n <= 0:
        return 0
    return n + sumofnatural(n - 1)
if __name__ == "__main__":
    n = int(input("Enter a natural number: "))
    print(f"Sum of first {n} natural numbers : {sumofnatural(n)}")