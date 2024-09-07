x="RitiKShArMa"
a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
c=""
for i in range(len(x)):
    z=x[i]
    for j in range(len(a)):
        l=a[j]
        if z==l:
            c=c+b[j]
print(c) 


txt = "xyz"
  
b=''
for i in txt:
    if i ==  'y':
        b=b+'ritik'
    else:
        b=b+i
print(b)
    




