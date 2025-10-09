# x=10,y=3,z=5
# if(x>y) and (x>z):
#     print("x is greater")
# elif (y>z) and (y>x):
#         print("y is greater")
# else:
#         # print("z is greater")
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
 sum_digits += num % 10
 num //= 10
print("Sum of digits is:", sum_digits)