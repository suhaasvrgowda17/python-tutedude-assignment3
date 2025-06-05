def factorial(i):
    if i==0 or i==1:
        return 1
    else:
        return i*factorial(i-1)
n=int(input("Enter a number: "))
i=factorial(n)
print("Factorial of ",n," is ",i)
