a = float(input("Input number: "))

if a%3 == 0 and a%5 == 0:
    print(f"{a} is divisible by 3 and 5")
elif a%3 and a%5 != 0:
    print(f"{a} is divisible by 3")
elif a%3 != 0 and a%5 == 0:
    print(f"{a} is divisible by 5")
else:
    print(f"{a} is not divisible by 3 or 5")