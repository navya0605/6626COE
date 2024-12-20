def factorial(n):
    if n==0 or n==1:
        return 0
    else:
        return n*factorial(n-1)
n=int(input("enter a number"))
print(factorial(n))