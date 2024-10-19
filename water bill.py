units = int(input("Enter water consumption in units: "))
if units <= 50:
    bill = units * 0.30
elif units <= 100:
    bill = (50 * 0.30) + ((units - 50) * 0.50)
else:
    bill = (50 * 0.30) + (50 * 0.50) + ((units - 100) * 0.80)
print(f"Total water bill: ${bill:.2f}")
