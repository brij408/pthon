a=[7,2,4,2,7,9]
b=[]
for  i in range(len(a)):
    x=a[i]
    if x not in b:
        b.append(x)
print(b)

a=[1,2,3,7,10,1,11,12]
for i in range(len(a)):
    if a[i] + a[i*1] == a[i+2]:
        print(a[i],a[i-1],[a+2])