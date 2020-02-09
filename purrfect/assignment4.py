# prime number********************************
'''

x=int(input('enter a number'))
s=range(2,x)
for i in s:
    if x%i==0:
        print('non prime')
        break
else:
    print("prime")

'''
        
#print first n prime number*********************
'''
x=int(input('enter a number'))
s=range(2,x)
for i in s:
    if x%i==0:
        continue
    else:
        print('')

'''
# next prime number to a given number********************
a=int(input('enter smaller number'))
b=int(input('enter larger number'))
s=range(a,b)
for x in s:
    for num in range(2,x):
        if x%num==0:
           break
    else:
        print('%d is a prime number' %x)
else:
    print('no prime number %d and %d' %(a,b))
