
def print_range(start, end):
    if start == end:
        print(start)
        return
    print(start)
    step = 1 if start < end else -1
    print_range(start + step, end)

if __name__ == "__main__":
    s = input("Enter one number (n) or two numbers (start end): ").strip().split()
    if not s:
        print("No input provided.")
    elif len(s) == 1:
        start, end = 1, int(s[0])
        print_range(start, end)
    else:
        start, end = int(s[0]), int(s[1])
        print_range(start, end)
