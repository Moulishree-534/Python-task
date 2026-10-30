#count numbers
##n=int(input("enter a num"))
##c=0
##while n>0:
##    n=n//10
##    c=c+1
##    print('count=',c)

###count and sum the input
##n=int(input("enter a num"))
##d=1
##while d<=n:
##    d=d+1
##    if n%d==0:
##        print(d)

##n=int(input("enter a num"))
##d=1
##count=1
##while d<=n:
##    d=d+1
##    if n%d==0:
##        count=count+1
##        print(d)
##print(count)
##
#num qub values
##a=int(input("enter a num"))
##while a>0:
##    l=a%10
##    print(l)
##    a=a//10
##    print(a)
##    num=a**3
##    print(a,"=",num)
##    print(l,"=",l**3)
##    

##i = 1
##while i <= 5:
##    print(i)
##    i += 1
##i = 2
##while i <= 10:
##    print(i)
##    i += 2
##i = 1
##while i <= 9:
##    print(i)
##    i += 2
##i = 1
##total = 0
##while i <= 3:
##    total += i
##    i += 1
##print("Sum:", total)
#calculate table
##n = int(input("Enter a number: "))
##i = 1
##while i <= 10:
##    print(n, "x", i, "=", n * i)
##    i += 1
###positive number  digit count
##n = int(input("Enter a positive number: "))
##count = 0
##while n > 0:
##    count += 1
##    n //= 10
##print("Digits:", count)
#positive number digit sum of all numbers
##n = int(input("Enter a positive number: "))
##total = 0
##while n > 0:
##    digit = n % 10
##    total += digit
##    n //= 10
##print("Sum of digits:", total)
#armstrong numbers
##t=0
##n=int(input("enter a num"))
##original=n
##while n>0:
##    d=n%10
##    t = t+d**3
##    n//=10
##print(t)
##if original==t:
##        print("it is armstrong")
##else:
##    print("it is not armstrong number")

##        
##secret = 7
##guess = 0
##while guess != secret:
##    guess = int(input("Guess the number: "))
##print("Correct guess!")



##password = input("Enter password: ")
##while password != "python123":
##    password = input("Enter password: ")
##    print("Access granted!")

##n=int(input("enter a num"))
##t=0
##while n>0:
##    digit=n%10
##    t=t+d
##    n//=10
##print("sum of digits:",total)


##n = int(input("Enter a positive number: "))
##total = 0
##while n > 0:
##    digit = n % 10
##    total += digit
##    n //= 10
##print("Sum of digits:", total)
##

##a=input("enter a word")
##print(a)
##reverse=a[: : -1]
##print(reverse)
##if a==reverse:
##    print("it is palindrome")
##else:
##    print("it is not a palindrome")
##
##Write a program that reads a set of integers, and then prints the sum of the even and odd integers.
##count_even=0
##count_odd=0
##sum_even=0
##sum_odd=0
##a=int(input("enter a num"))
##while a>0:
##    b=a%10
##    if b%2==0:
##        count_even+=1
##        sum_even+=b
##    else:
##        count_odd+=1
##        sum_odd+=b    
##    a=a//10
##
##print("even=",count_even)
##print("odd=",count_odd)
##print("sum of even number=",sum_even)
##print("sum of odd number=",sum_odd)
##
##


##count1=0
##sum1=0
##count2=0
##sum2=0
##a=int(input("enter a num"))
##while a>0:
##    b=a%10
####    print("b=",b)
##    if b<=5:
##        count1+=1
##        sum1+=b
##    else :
##       b<=10
##       count2+=1
##       sum2+=b
##       
##    a//=10
##print("count1=",count1)
##print("count2=",count2)
##print("sum of sum=",sum1)
##print("sum of sum=",sum2)
##       
##
