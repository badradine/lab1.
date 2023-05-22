a= int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))

import math
d = ((b**2)-(4*a*c))

x1 = (-b+e)/(2*a)
x2 = (-b-e)/(2*a)

if d==0:
    e=math.sqrt(d)
    x1 = (-b + e) / (2 * a)
    x2 = (-b - e) / (2 * a)
    print("The value of x is:", x1)
elif d<0:
    print("No result")
else:
    e=math.sqrt(d)
    x1 = (-b + e) / (2 * a)
    x2 = (-b - e) / (2 * a)
    print("The roots of x are:", x1,"and", x2)
