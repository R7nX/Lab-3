from turtle import *



a = float(input("Input length 1: "))
b = float(input("Input length 2: "))
c = float(input("Input lenght 3: "))

if (a+b) > c: 
    if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2):
        print("The 3 line segments can form a right triangle.")
    elif a == b == c: 
        print("The 3 line segments can form a equilateral triangle.")
        for i in range(3):
            forward(a)
            left(120)
        mainloop()
    else: 
        print("The 3 line sengments can form a triangle.")


else: 
    print("The 3 line segments cannot form a triangle.")