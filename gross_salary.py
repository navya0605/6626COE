salary=int(input('enter salary'))
if salary<=10000:
    HRA=salary*67/100
    DA=salary*73/100
elif 10000<salary<=20000:
    HRA = salary * 69 / 100
    DA = salary * 76 / 100
else:
    HRA = salary * 73 / 100
    DA = salary * 89 / 100
GS = HRA + DA + salary
print(f'gross salary is {GS}')