
def print_desc(n):
    if n <= 0:
        return
    print(n)
    print_desc(n - 1)

if __name__ == "__main__":
    print_desc(5)
