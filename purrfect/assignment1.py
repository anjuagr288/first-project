#area of circle********************************
'''
r=input("enter radius:")
area=((22/7)*int(r)*int(r))
print("area of circle",area)
'''

#volume of cuboid****************************************
'''
l=input("enter length:")
b=input("enter breadth:")
h=input("enter height:")
vol=int(l)*int(b)*int(h)
print("volume of cuboid",vol)
'''

#square of number****************************************
'''

r=input("enter a number:")
square=(int(r)*int(r))
print("square of number is",square)
'''

#area of triangle********************************************


l=input("enter side one:")
b=input("enter side two:")
h=input("enter side three:")

l=int(l)
b=int(b)
h=int(h)
print("sides are: l=%d, b=%d and h=%d" %(l,b,h))
s=(l+b+h)/2
area=(s*(s-l)*(s-b)*(s-h))**0.5
print("%f of triangle is" %area)




