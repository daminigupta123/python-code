val = 0xCAFE
last4 = val & 0xF
at_least_three = bin(last4).count("1") >= 3
print(at_least_three)
