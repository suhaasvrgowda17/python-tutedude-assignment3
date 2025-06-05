import math
n=float(input("Enter any number: "))

if n>=0:
    print("Square root of ", n," is ",math.sqrt(n))
else:
    print("Square root of ",n," is undefined")
if n>0:
    print("Logarithm of ",n," is ",math.log(n))
else:
    print("Logarithm of ",n,"is not is undefined")

r=math.radians(n)
print("Sin of ",n," is ",math.sin(r))

