
inches = float(input("Enter measurement in inches: "))
#formula is :
feet = inches / 12
yards = inches / 36
centimetres = inches * 2.54
meters = inches / 39.37

print(f"{inches} inche = {feet:.2f} feet")
print(f"{inches} inche = {yards:.2f} yards")
print(f"{inches} inche = {centimetres:.2f} centimetres")
print(f"{inches} inche = {meters:.2f} meters")
