num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

largest = num1 if (num1 >= num2 and num1 >= num3) else (num2 if num2 >= num3 else num3)
print(f"Largest number is: {largest}")