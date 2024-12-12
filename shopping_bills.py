#take salary from user
#take 3 shopping bills
#display total shopping amount
#% of amount spent on shopping feom salary
salary=int(input("give the salary"))
bill1=int(input("give bill1 "))
bill2=int(input("give bill 2 "))
bill3=int(input("give bill 3 "))
total_shopping_amount=bill1+bill2+bill3
print(f"total shopping amount is {total_shopping_amount}")
percentage=total_shopping_amount/salary*100
print(f" total shopping percentage is {percentage}%")