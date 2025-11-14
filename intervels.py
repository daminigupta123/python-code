x = float(input())
if 0 <= x <= 25:
    print("Interval is: [0,25]")
elif 25 < x <= 50:
    print("Interval  is :(25,50]")
elif 50 < x <= 75:
    print("Interval is :(50,75]")
elif 75 < x <= 100:
    print("Interval is : (75,100]")
else:
    print("Out of Intervals")
