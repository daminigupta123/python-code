
# sum_two = lambda x, y: x + y
# 
sum_digits = lambda n: sum(map(int, str(abs(int(n)))))

if __name__ == "__main__":
    # a = float(input("Enter first number: "))
    # b = float(input("Enter second number: "))
    # print("Sum:", sum_two(a, b))

    n = input("Enter a digits: ")
    print("Sum of digits is:", sum_digits(n))