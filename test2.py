a='hello my name is brij'
b=a.find('name')
print(b)


a=[2,3,1,4,6,]
a.sort()
print(a[0])




# a= "my name is brij"
# b=a[ :-16:-1]
# print(b)

a=input('enter the first number' )
b=0
for i in range(len(a)):
    b=b+int(a[i])
print(b)
    

        
        
      
             
         

a=[1,2,3,4,6,6,7,7]
b=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]and a[i] not in b:
            b.append(a[i])
            print(b)
        
        
        
    
a=int(input('enter the number:'))
for i in range(1,11):
        print(f"{a}*{i}={a*i}")        
            


a=[9,8,7,6,4,3,2,1]

for i in range(len(a)):
    x=a[i]
    for j in range(len(a)):
        z=a[j] 
        if x<z:
            c=a[i]
            a[i]=a[j]
            a[j]=c
            
print(a)            





a=[[7,6,5,4,3,2],[3,2,1],[9,8,7,6]]
c=[]
for k in a:
    for i in range(len(k)):
        x=k[i]
        for j in range(len(k)):
            y=k[j]
            if k[i]<k[j]:
                c=k[i]
                k[i]=k[j]
                k[j]=c
print(a)                

a='my name is brij'
b=a.rfind('name')
print(b)



for i in range(1,1000+1):
    if i%2!=0:
        print(i,'is odd number') 


a={
    'remaesh':70,
    'ganesh':50,
    'ramo':70,
    'sham':50
}

b=list(a.values())
d=0
c=[]
for i in range(len(b)):
    if b[i] not in c:
      
      c.append(b[i])                               
    else:
      d+=b[i]
      print(b[i],'is dupilcate')
      
print(d)      

a={1,2,3,4,5,6}
b={1,7,8,9}
c=a.union(b)
print(c)

a=[1,2,3,4,5,6]
b=[7,8,9]
c=a.extend(b)
print(c)
      
      
a={1,2,3,4,5}    
b={2,3,4,5,6}  
c=a.symmetric_difference(b)
print(c)

a={1,2,3,4,5}    
b={2,3,4,5,6}  
a.symmetric_difference_update(b)
print(a)


a={1,2,3,4,5,6,}
b={4,5,6,7,8}
a.setdefault(b)
print(a)



    


















