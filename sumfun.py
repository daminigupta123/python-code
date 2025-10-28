def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication") 
    print("4. Division")
    
    choice = input("Enter choice (1/2/3/4): ")

    match choice:
        case "1":
            print(f"Result: {add(num1, num2)}")
        case "2":
            print(f"Result: {subtract(num1, num2)}")
        case "3":
            print(f"Result: {multiply(num1, num2)}")
        case "4":
            print(f"Result: {divide(num1, num2)}")
        case _:
            print("Invalid choice")