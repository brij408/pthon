a={1,2,2,3,3}
print(a)                #duplicate number print nahi kere ga set{}
                         #indexing is not allowed


#first method 
a={1,2,3,4,5}
b={2,4,6,1,3}
c=a.difference(b)
d=b.difference(a)
print(c)
print(d)


a={1,2,3,4,5,6,7}
b={2,4,6,1,3}
a.difference_update(b)
print(a)


#intersection
a={1,2,3,4,5}
b={1,5,6,7,8}
c=a.intersection(b)
print(c)

#intersection update
a={1,2,3,4,5}
b={2,4,5,8,9}
a.intersection_update(b)
print(a)
