a=(1,2,3,4,5,5,6,)
b=a.count(5)
c=a.index(4)
print(b)
print(c)

#method for changing tuple
#first method

a=(1,2,3,4,5)
b=list(a)
b.append(5)
c=tuple(b)
print(c)

#2nd method
a=(1,2,3,4,5)
b=a+(1,)
print(b)

# 3rd slicing method
a=(1,2,3,4,5)
b=a[0:2] +(1,)+a[2:]
print(b)

#ittration

a='ritik'
for i in a:
    print(i,end='')


a=(1,2,3,4)
b=list(a)
b.append(2)
c=tuple(b)
print(c)