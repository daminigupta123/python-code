
X = input().strip()
if X.isdigit():
    print("IS DIGIT")
elif X.isalpha():
    print("ALPHA")
    if X.isupper():
        print("IS CAPITAL")
    else:
        print("IS SMALL")
