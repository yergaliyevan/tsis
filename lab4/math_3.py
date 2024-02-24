import math
n=int(input("number of sides:"))
l=int(input("length of sides:"))
a=l/(2*math.tan(math.pi/n))
s=int((n*l*a)/2)
print("area of the polygon is:",s)
