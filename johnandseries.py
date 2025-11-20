
a = int(input("first term: "))
d = int(input(" difference: "))
n = int(input("term number: "))
nth_term = a + (n - 1) * d
sum_numbers= (n * (2 * a + (n - 1) * d)) // 2
print("Nth term:", nth_term)
print("n terms additon:", sum_numbers)