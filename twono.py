import math
A, B = map(int, input().split())
result = A / B
print(f"floor {A} / {B} = {math.floor(result)}")
print(f"ceil {A} / {B} = {math.ceil(result)}")
print(f"round {A} / {B} = {round(result)}")
