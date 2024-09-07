x="RitiKShArMa"
a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
b="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
c=""
for i in range(len(x)):
    z=x[i]
    for j in range(len(a)):
        l=a[j]
        if z==l:
            c=c+b[j]
print(c) 

x="RitiKShArMa"
a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
c=""
for i in range(len(x)):
    z=x[i]
    for j in range(len(a)):
        l=a[j]
        if z==l:
            c=c+b[j]
print(c) 




