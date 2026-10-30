##a=int(input("enter a marks"))
##if a>=35:
##    print("student pass")
##else:
##    print("student fail")
'''
a=int(input("enter your tamil marks"))
b=int(input("enter your english marks"))
c=int(input("enter your maths marks"))
d=int(input("enter your science marks"))
e=int(input("enter your socail marks"))
total=a+b+c+d+e
print(total)
i=total/5
print(i)
if i>35:
    if i>95 and i<=90:
        print("grade O")
    elif i>70 and i<90:
        print("grade A")
    elif i>=50 and i<=69:
        print("grade B")
    elif i>40 and i<=50:
        print("grade C")
    else:
      print("no grade")
else:
        print("student fail")

if a>b and a>c and a>d and a>e:
    print("you scored highest mark=","in tamil")
elif b>a and b>c and b>d and b>e:
    print("you scored highest mark=","in english ")
elif c>a and c>b and c>d and c>e:
    print("you scored highest mark=","in Maths ")
elif d>a and d>b and d>d and d>e:
    print("you scored highest mark=","in Science ")
else:
    print("your scored highest mark=","in Social ")'''


    
##elif average>=75:
##    print("grade A")
##elif average<=70:
##    print("grade B")
##    
##    
##        


'''total=0
for i in range (1,6):
    a=int(input("enter a mark"))
    total=total+a
    print(total)
print(total)
'''
##m=6
##number=1
##upper_case =1
##lower_case=1
##special_char
##a=input("enter a password")
##print(len(a))
##while True:
##    a=input("enter a password")
##    if len(a)>=6:
##        print(a)
##    else:
##        break
##    
##
##for i in range(1,6):
##    for j in range(5-i):
##        print("",end= " ")
##    for j in range(i):
##        print("* ",end="")
##    print()

##for i in range(1,7): #i=1 2
##    for j in range(6-i):
##        print("",end= " ")
##    for j in range(i): #0,1 0,2
##        print(j,end="")
##    print()

##for i in range(1,7,1): #i=1 2 3
##    for j in range(6-i):
##        print("",end= " ")
##    for j in range(1,i+1): #1,1 1,2 1,3
##        print(j,end="")
##    print()

##for i in range(1,7): #i=1 2 3
##    for j in range(7-i):
##        print(" ",end= " ")
##    for j in range(i): #1,1 1,2 1,3
##        print("* ",end=" ")
##    print()
##
##n=6
###2
##for i in range (1,7):#i=4
##    for j in range (i):
##        print(" ",end= " ")#__
##    for j in range (1,n):#
##        print("* ",end = " ")
##    print()
##    n=n-1

    
##n=6
##for i in range(1,7):
##    for j in range(i):
##        print(" ",end=" ")
##    for j in range(1,n):
##        print("* ",end=" ")
##    print()
##    n=n-1
##
'''for i in range(1,5): #i=1 2 3
    for j in range(5-i):
        print(" ",end= " ")
    for j in range(1,i+1): #1,1 1,2 1,3
        print(j,end=" ")
    print()
n=4
for i in range (1,5):#i=4
    for j in range (i):
        print(" ",end= " ")#__
    for j in range (1,n):#
        print(j,' ',end = "")
    print()
    n=n-1'''

##for i in range(1,5): #i=1 2 3
##    for j in range(5-i):
##        print(" ",end= " ")
##    for j in range(1,i+1): #1,1 1,2 1,3
##        print(j,end=" ")
##    print()
##n=3
##for i in range (1,5):#i=4
##    for j in range (i):
##        print(" ",end= " ")#__
##    for j in range (n,0,-1):#
##        print(j,' ',end = "")
##    print()
##    n=n-1

##primited
for i in range(5,0,-1):
    for j in range(i):
        print(" ",end= " ")
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()

n=4
for i in range (1,5):#i=4
    for j in range (i):
        print(" ",end= " ")#__
    for j in range (n,0,-1):#
        print(j,' ',end = "")
    print()
    n=n-1


