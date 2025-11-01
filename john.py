#input
a = float(input("Enter  first term (a): "))
d = float(input("Enter  common difference (d): "))
n = int(input("Enter  number of terms (n): "))


nth_term = a + (n - 1) * d

sum_n = (n / 2) * (2 * a + (n - 1) * d)

print("Nth term of the series:", nth_term)  #results
print("Sum of first n terms:", sum_n)
