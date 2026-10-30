#without argument
##def function_add():
##    a=10
##    b=20
##    c=a+b
##    print(c)
##
##function_add()
##
###with argument
##def hello(name):
##    print("welcome ",name)
##
##hello('priya')
##
###positional argument
##def fun(name,age):
##    print("hello",name,"your are",age,"years old")
##
##fun("shri",20)
##
###default argument
##def num (x=20,y=30):
##    print("X=",x)
##    print("Y=",y)
##
##num(10,40)

##key argument
def fun (name,age):
    print("hello",name,"your are",age,"years old")

fun("mouli", 20)
fun(age=10,name="Ajay")

#variable lenth argument *tuple()
##def a(*n):
##    print(n)
##
##a(60)
##a(100,140)
##a('app',14,7.9)
###dictionary
##def a(**n):
##    print(n)
##
##a(no=1,age=34,name='priya')
##a(n1=43,n2=87)
#function task
#Create a function to check whether a number is positive, negative, or zero
##def check_number(n):
##    if n > 0:
##        print("positive number")
##    elif n<0:
##        print("negative number")
##    else:
##        print("zero")
##        
##
##check_number(5)
##check_number(-1)
##check_number(0)
##Develop a function to determine whether a given year is a leap year.
##def check_leapyear( n):
##    if n % 4==0:
##        print("it is leap year")
##
##check_leapyear(2004)

###implement a function to find the largest among three numbers
##def largest_number(a,b,c):
##   if  a>b and  a>c:
##        print("A is geater")
##   elif b>a and b>c:
##         print("B is geater")
##
##   elif c>a and c>b:
##       print("C is geater")
##    
##largest_number(10,20,4)
###Write a function to check whether a number is even or odd.
##def check_evennumber(a):
## if a%2==0:
##    print("it is even number")
## else:
##    print("it is odd number")
##
##check_evennumber(5)
#Design a function to assign grades based on student marks.
##def check_studentmark(a):
## if a>=90 and a<=99:
##     print("your A grade")
## elif a>=80 and a<=89:
##    print("your  B grade")
## elif a>=70 and a<=79:
##     print("your C grade")
## else:
##    print("your D grade")
##
##
##check_studentmark(93)
###Create a function to print the multiplication table of a given number.
##def check_multiplicationtable(n):
##    a=1
##    while a<=10:  
##        print(n,"x",a,"=",n*a)
##        a=a+1
##
##n=int(input("enter a n"))
##a=1
##while a<=10:
##    
##    print(n,"x",a,"=",n*a)
##    a=a+1
      
##check_multiplicationtable()
#Create a function to check whether a number is zero.
##def check_numberzero(a):
##    if a<=0:
##        print("number is zero")
##    else:
##        print("it is number")
##
##check_numberzero(25)
##Create a function to check if number is prime#doubt
##def check_primenumber(a):
##    if a==2:
##        print("it is prime number")
##
##
##check_primenumber()
##
#Create a function to count the digits in a given number.
##n=int(input("enter a number"))
##def countdigit_number(n):
##    c=0
##    while  n>0:
##         c=c+1
##         n=n//10  
##    print('count=',c)
##
##countdigit_number(n)
#Implement a function to reverse a string
##a=input("enter a word")
##def reverse_string(a):
## 
#### print(a)
## reverse=a[ : : -1]
## print(reverse)
##
##reverse_string("computer")
#Create a function to check whether a string is a palindrome
##a=input("enter a word")
##print(a)
##def reverse_string():
##   
##    reverse=a[ : : -1]
##    print(reverse)
##    if a==reverse:
##        print("it is palindrome")
##    else:
##        print("it is not panlindrome word")
##
##reverse_string()
#Develop a function to count vowels in a string.
##n=input("enter a words")
##def count_vowels(n):
##    c=0
##    for b in n:
##        if b=="a" or b=="e" or b=="i"  or b=="o" or b=="u":
##         c=c+1
##         print(c)
##
##
##count_vowels(n)

##Create a function to count the number of words in a sentence
##a=input("enter a word")
##def countnumber_words():
##    d=a.count(' ')
##    print(d+1)
##
##countnumber_words()
##
#Write a function to find the sum of all natural numbers up to N
##a=int(input("enter a number"))

##def natural_number():
##    a=1
##    for i in range (1,6,1):
####        print(i)
##        a=a+i
##    print(a)
##        
##
##natural_number()


### factorial
##def natural_number():
##    a=1
##    for i in range (1,6,1):
####        print(i)
##        a=a*i
##    print(a)
##        

##natural_number()

#Create a function to check if number is prime.
##n=int(input("enter a number"))
##d=1
##c=0
##while d<=n:
##    if n%d==0:
##        print(d)
##        c=c+1
##    d=d+1
##print(c)
##if c<=2:
##    print("it is prime number")
##else:
##    print("it is not a prime number")
## 
##
