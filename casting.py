a= input('enter the number')
b=0
for i in range(len(a)):
    b=b+int(a[i])
print(b)    

a=[2,3,7,9,4,6]

for i in range(len(a)):
    x = a[i]
    for j in range(len(a)):
        y = a[j]
        if x<y:
            c=a[i]
            a[i]=a[j]
            a[j]=c
print(a)   



 



a=[1,2,3,4,5]
b=[2,3,4,5,6] 
for i in a:
    for j in b:
        if i==j:
            
            print(i)
        