a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
d = int(input("Enter side 4: "))

if a == b == c == d:
    print("Square")
elif a == c and b == d:
    print("Rectangle")
else:
    print("Other quadrilateral")
