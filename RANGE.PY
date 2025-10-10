# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
# start = int(input("Enter start number: "))
# end =int(input("Enter end number: "))
# print(f"Prime numbers between {start} and {end}:")
# for num in range(start, end + 1):
#     if is_prime(num):
#      print(num)
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)