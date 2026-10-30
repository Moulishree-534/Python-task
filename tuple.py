'''#tuple
a=1
a=1,
a=1,'a',4,'apple',1,True,'a',123,123,4
print(a)
print(a,type(a))
#count
c=a.count(4)
print(c)
#index
print(a.index(1,3))
#to change in tuple
b=list(a)
print(b,type(b))
b.append(2)
c=tuple(b)
print(c,tuple(c))
#membership operator
if 4 in a:
    print("found")
'''
#set
a={1,'1','a','laptop','app'}
b={'app'}
'''print(a)
print(b)
#add-add,update
a.add('phone')
print(a)
a.update(b)
a.update('phone')
print(a)
#delete,remove discard
#remove
a.remove('a')
print(a)
##a.remove('ab')
##discard
a.discard('ac')
print(a)
##pop
a.pop()
print(a)
a.pop(2)
print(a)
'''

#union set
##print(a.union(b))
##print(a)
##print(a.intersection(b))
##print(a.difference(b))
##print("syy_diff",a.symmetric_difference(b))
##a.symmetric_difference_update(b)
##print(a)
##print(a.isdisjoint(b))
##print(a.issuperset(b))
##print(a.issubset(b))
#copy
##num=[14,29,50,8,4,100]
##print("num=",num)
##n=num.copy()
##print("num=",n)
##num.append('a')
##print("after append in num",num)
##print("after append in 'n'",n)
###add element
##a='note'
##b='book'
##print(a+b)
##list1=['apple','cat',100,14.29,100]
##print(list1)
##num=[14,29,50,8,4,100]
##print(num)
##print(list1+num)

#task
##Write a Python program to create a tuple with different data types
##a=1,'a',5,6,"apple",4.02,True
##print(a)
###Write a Python program to create a tuple of numbers and print one item
##a=1,33,45,65,78,90,25,78
##print(a)
##b=int(input("enter a num"))
##print(a[b])
# Write a Python program to add an item to a tuple
'''a=1,'a',4,'apple',1,True,'a',4
print(a)
b=list(a)
print(b,(type(b)))
b.append(6)
print(b)
c=tuple(b)
print(c,tuple(c))
#.Write a Python program to find the index of an item in a tuple
a=1,'a',4,'apple',1,True,'a',4
print(a.index('apple'))'''
#6.Write a Python program to find the length of a tuple
##a=1,'a',4,'apple',1,True,'a',4
##print(len(a))
###.Write a Python program to reverse a tuple
##a=1,'a',4,'apple',1,True,'a',67
##r=a[ : :-1]
##print(r)
###.Write a Python program to find repeated items in a tuple
##a=1,'a',4,'apple',1,True,'a',4
##for i in a:
##    c=a.count(i)
##    if c>=2:
##        print(i)
##        
##        
###Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
##a=1,3,5,7,9,2,4
##m=1
##for i in a:
##    m=m*i
##print(m)
#Create a tuple of squares of numbers 1–10
##a=1,3,5,7,9,2,4
##for i in a:
##    print(i,'=',i**2)

#.Write a Python program to unpack a tuple into several variables.
a=1,'a',4
b,c,d=a
print(b)
print(c)
   
    
    

##b=b*a
##print(b)
##list1=['apple','cat',100,14.29,100]
##c=list1.count(100)
##print(c)


