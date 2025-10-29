
def fib(n, memo={0: 0, 1: 1}):
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

if __name__ == "__main__":
    print("First 20 Fibonacci numbers (recursion):")
    for i in range(10):
        print(fib(i))
