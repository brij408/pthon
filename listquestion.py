# a=[1,2,3,4,5]
# c=a[4]
# a[4]=a[0]
# a[0]=c
# print(a)


# a=[1,2,3,4,5,6]
# c=a[3]
# a[3]=a[1]
# a[1]=c
# print(a)

# a=['brij','rana','mohan','singh']     
# c=a[2]
# a[2]=a[0]
# a[0]=c
# print(a)


# a=[1,2,3,4,5]
# b=len(a)
# print(b)

# a=input('enter the first number')
# b=input("enter the second number")
# if a>=b:
#     print(a)
# else:
#     print(b)

# a=input('enter the first number')
# b=input("enter the second number")
# if a<=b:
#     print(a)
# else:
#     print(b)


# a=[1,2,3,4,5]
# a.count(3)
# print(a)

# a=[1,2,3,4]
# a.reverse()
# print(a)

# a=[1,2,3,4]
# a.clear()
# print(a)

# a=[1,2,3,4]
# a.copy()
# print(a)

# a=[1,2,3,4,5]
# a.count(3)
# print(a)

# a=[1,2,3,4,5]
# c=0
# for i in range(len(a)):
#     c=c+i
    
#     avg=c/len(a)
#     print(c)
#     print(avg)
    
# a=[1,2,3,4,5]
# c=0
# for i in a:
#     c=c+i
    
    
#     print(c)
    
    
    
a=[1,2,3,4,5]
c=1
for i in range(len(a)):
    c=c*i
    
    
    print(c)
        
# a=[1,2,4,3,5] 
# a.sort()
# print(a[0])



# a=[1,2,4,3,5] 
# a.sort()
# print(a[-1])

        
# a=[1,2,4,3,5] 
# a.sort()
# print(a[-2])


# a=[1,2,3,4,5,6,7]

# for i in a:
    
#     if i % 2==0:
#          print(i, 'is even')
#     else:
#         print(i,'is odd')
        

# for even_numbers in range(4,15,2):

# 	print(even_numbers,end=' ')


# Python program to print odd Numbers in given range

# start, end = 4, 19


# for num in range(start, end + 1):
    
    
#     if num % 2 != 0:
#         print(num, end = " ")


    
        
        
# a=[1,2,3,4,5,6,7]

# for i in a:
#     x=a[i]
#     if x % 2==0:
#          print(i, 'is even')
#     else:
#         print(i,'is odd')      
        
        
        
        
        

# list1 = [11, -21, 0, 45, 66, -93]                     #phele kiya hai wah se dekh lena


# for num in list1:
    
#     if num >= 0:
#         print(num, end=" ")





# # Python program to print positive Numbers in given range 

# start, end = -4, 19

# # iterating each number in list 
# for num in range(start, end + 1): 

# 	# checking condition 
# 	if num >= 0: 
# 		print(num, end=" ") 

        
# a=[2,34,3,54,6,7,8,2,3,8]
# c=[]
# for i in range(len(a)):
#     for j  in range(i+1,len(a)):
#         if a[i]==a[j] and a[i] not in c:
#             c.append(a[i])
# print(c)            
                    
                    
# a=[(),'r',1,3 ]
# b=[]
# for i in range(len(a)):
#     x=a[i]
#     if len(x)>0:
#         b.append(x)
#         print(b)
             
    
    
    
# a=[1,2,3,4,5,6]
# for i in  range(len(a)) :
#     x=a[i]
#     for j in range(len(a)):
#         z=a[j]
#         if x<z:
#             c=a[i]
#             a[i]=a[j]
#             a[j]=c
# print(a)            
            
# a=[(),1,4,[]]
# b=[]
# for i in a:
#     if i!=():
#         b.append(i)
# print(b)                            
                    
                    
# a=[i for i in range(10) if i%2==0]
# print(a)                    

# a=[4*i for i in range(1,11) ]
# print(a)


# a=[(),'1','2',[]]
# b=[]
# for i in a:
#     if len(i)>0:
#         b.append(i)
# print(b)        


# a=[10,1,2,120,60,70]
# b=[]
# for i in a:
#     if i%10==0:
#         b.append(i)
# print(b)


# a=(1,2,3,4)
# b=list(a)
# b.append([])
# c=tuple(b)
# print(c)

a= input('enter the number')
b=int(a)

x=1
for i in range(1,b+1):
    x=x*i
print(x)

