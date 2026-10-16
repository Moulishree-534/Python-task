bitwise opertors
'''a=20  #10100
b=5   #00101
print(a&b) #00100
print(bin(a))

a=10 #1010
b=5  #0101
print(a|b) #1111

a=15  #1111
b=8   #0101
print(~a)#a=a+1
print(~b)'''

'''a=10 #1010
b=5   #0101
print(a^b)'''

'''a=20
b=5
print(a>>3)
print(a<<3)'''
'''for i  in range (1,5):
    print(i)
else:
    print("completed")'''

'''a=int(input("enter a num")) #3
d=0 #dummy variable to add numbers
i=1 
while i<=a: #1<=3 2<=3 #3<=3 #4<=3
    d=d+i #0+1=1 #1+2=3 #3+3=6
    i=i+1 #1+1=2 #2+1=3 #3+1=4
print(d)'''
##d=0 #dummy variable to add numbers
##for i in range(1,a+1):
##    d=d+i
##print(d)

'''a=int(input("enter a num")) #3
d=0 #dummy variable to add numbers
i=1
while i<=a:
    d=d+i
    i=i+1
    print(d)'''
'''a=int(input("enter a num")) #3
d=0 #dummy variable to add numbers
i=1
while i<=a:
    d=d+i  #1<=3 #2<=3#3<=3#4<=3
    i=i+1#0+1=1 #1+2=3 #3+3=6#3+4=9
    print(d)#1+1=2#2+1=3#3+1=4#4+1=5'''
'''a=int(input("enter a num"))
a<11
while a<=10:
        print(a)
        a=a+1'''
'''a=int(input("enter a num"))
a=5
while a>0:
        print(a)
        a=a-1'''
'''a=int(input("enter a num"))
d=0
i=1
while i<=a:
    d=d+i
    i=i+1
    print(d)'''

'''a=int(input("enter a num"))
while a<=10:
    print(a,"x",3,"=",a*3)
    a=a+1'''
##while loop password checking
##a=int(input("password"))
##b=1234
##while b!=a:
##    print("enter password again")
##    a=int(input("password"))

##for loop password checking
##a=int(input("password"))
##b=1234
##if b!=a:
##    for i in range(1,4):
##        print("enter password again")
##        a=int(input("password"))
##    print("phone locked")
##count of digit
##n=int(input("enter a number"))
##c=0
##while n>0:
##    n=n//10
##    c+=1
##    print('count=',c)

##factors of numbers
##n=int(input("enter a number"))
##d=1
##while d<=n: 
##    if n%d==0: 6%1
##        print(d)
##    d=d+1 
n=int(input("enter a number"))
d=1
count=0
while d<=n:
    if n%d==0:
       count=count+1
    d=d+1
print(count)



