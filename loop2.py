# x="brijmohan"
# a="abcdefghijklmnopqrstuvwxyz"
# b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# c=""
# for i in range(len(x)):
#     y=x[i]
#     for j in range(len(a)):
#         z=a[j]
#         if y==z:
#             c=c+b[j]
# print(c)             
           
        
x='brij'
b='abcdefghijklmnopqrstuvwxyz'
c='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d=''
for i in range(len(x)):
    y=x[i]
    for j in range(len(b)):
        z=b[j]
        if y==z:
            d=d+c[j]
print(d)            
               
        
