#electricity calculation based on individual product price
def electricity_bill(units):
    if units <= 50:
        return units * 0.50
    elif units <= 150:
        return 25 + (units - 50) * 0.75
    elif units <= 250:
        return 100 + (units - 150) * 1.20
    else:
        return 220 + (units - 250) * 1.50

units = int(input("Enter the number of units: "))
bill = electricity_bill(units)
print("The electricity bill is: ", bill)
