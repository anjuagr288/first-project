#********************************************check even odd
'''
if float(input('enter a number:'))%2==0:
    print('even')
else:
    print('odd')
'''
#*********************greatest of three no
'''
print('enter three numbers')
x=int(input())
y=int(input())
z=int(input())
if x>y and x>z:
    print('%d is greatest' %x)
elif y>x and y>z:
     print('%d is greatest' %y)
elif z>x and z>y:
     print('%d is greatest' %z)
elif x==y and x==z:
     print('%d,%d and %d all are equal' %(x,y,z))
'''
#number of dats in a month**********************************
'''
x=int(input('enter numeric value of month:'))
if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
    print('this month ha 31 days')
elif x==4 or x==6 or x==9 or x==11:
    print('this month ha 30 days')
'''
# caculate amrks and percentage******************************
'''
q,w,e,r,t=int(imput())
'''
#complexnumber **************************************************
c=complex(input("enter a complex number "))
if c.real>c.imag:
    print('real part is greater')
if c.real == c.imag:
    print('real part is equal to imaginary')
if c.real < c.imag:
    print('real part is greater')


