###.Write a Python program to remove item(s) from a given set
##a={1,'1','a','laptop',True,45.0,23,'s'}
##print(len(a))
##print(a)
##a.pop()
##a.remove('s')
##print(a)

#Write a Python program to remove an item from a set if it is present in the set.
##a={1,'app',34,78,'apple',}
##a.pop()
##print(a)

#.Write a Python program to create set difference
##a={1,'1','a','laptop',True,45.0,23}
##b={'a','laptop','app',12}
##print(a.difference(b))

###.Write a Python program to find the maximum and minimum values in a set
##a={12,100,34,67,84,90,45}
##print(min(a))
##print(max(a))

# Check if two sets are disjoint
##a={12,23,34,46,57,65}
##b={89,90,35,78,9}
##print(a.isdisjoint(b))

#  Find union, intersection, and difference between two sets.
##a={12,23,34,46,57,65}
##b={12,89,90,35,78,9}
##print(a.union(b))
##print(a.intersection(b))

###Find elements present in only one of two sets (symmetricdifference)
##a={34,45,78,12,43}
##b={12,87,90,67,89}
##print("syy_diff",a.symmetric_difference(b))

#Remove all elements divisible by 2 from a set of numbers
##a={34,45,78,12,43}
##b=list(a)
####print(b,type(b))
##for i in b:
##      if i%2==0:
##        print(i)
##        b.remove(i)
##print(b)
##c=set(a)
##print(c,set(c))

#.Write a Python program to remove all elements from a given in set
a={12,23,34,46,57,65}
set.clear(a)
print(a)

