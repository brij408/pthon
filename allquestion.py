# a= 'my name is brij'
# c=' '
# for i in range(len(a)):
#     c=c+a[i]
    
#     if a[i]==' ':
#         c=' '
# print(c)
        
# a='0123456789'
# b='7enfojdofgjoegjo37'
# c=0
# for i in range(len(b)):
#     if b[i]in a:
#         c=c+int(b[i])
# print(c)        

# import random
# wining_number=random.randint(1,50)
# for i in range(1,4):
#     guess_number=input('enter the number')
#     guess_number=int(guess_number)
#     if guess_number==wining_number:
#         print('you won',wining_number)
#         break
#     else:
#         print('you loss please try again')
#         if i==3:
#             print('game over',wining_number)


# --------letter ko capital mai kerna hai
# txt = "Hello my friends"

# x = txt.upper()

# print(x)
# ----------------------------------------

# x='brij'
# b='abcdefghijklmnopqrstuvwxyz'
# c='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# d=''
# for i in range(len(x)):
#     y=x[i]
#     for j in range(len(b)):     ase hi chot bhi hogaye ge
#         z=b[i]
#         if y==z:
#             d=d+c[j]
# print(d)            
    
# ------------sorting

# a=[3,2,1,5,7,8]
# for i in range(len(a)):
#     x=a[i]
#     for j in  range(len(a)):
#         y=a[j]    
#         if x<y:
#             c=a[i]
#             a[i]=a[j]
#             a[j]=c
# print(a)            
    

# # a=[[7,6,5,4,3,2],[3,2,1],[9,8,7,6]]
# # 
# # for k in a:
# #     for i in range(len(k)):
# #         x=k[i]
# #         for j in range(len(k)):
# #             y=k[j]
# #             if k[i]<k[j]:
# #                 c=k[i]
# #                 k[i]=k[j]
# #                 k[j]=c
# # print(a)                

# #append element in list
# # a=[1,2,3,4,5]
# # b=a.append(4)
# # print(b)

# # a=[1,2,3]
# # b=[1,2,3]
# # a.extend(b)
# # print(a)

# #---------------fibonacci series


# # a=[1,2,3,7,10,1,12]
# # for i in range(len(a)):
# #     if a[i]+a[i+1]==a[i+2]:
# #         print(a[i],a[i+1],a[i+2])
# #---------------------------------------------even odd

# # a=[1,2,3,4,5,6,6,7]
# # for i in range(len(a)):
# #     if i%2==0:
# #         print(i,'even')
# #     else:
# #         print(i,'odd')
# #--------------------------------------------

# # a=[1,-2,-3,-4]
# # for i in range(len(a)):
# #     if a[i] <=0:
# #         print(a[i],'negitive')
# #     else:
# #         print(a[i],'positive')
        
        
# # #------------------------------------------ reverse string or list

# # a='yoyo'
# # b=a[::-1]
# # print(b)


# # a=[1,2,3,4,5]
# # a.reverse()
# # print(a)

# # #--------remove empty tuple


# # a=[(),[],1,2,2,3]
# # for i in range(len(a)):
# #     if len(a[i])==0:
# #         a.remove(a[i])
# #         print(a)        
        
# # #list compression----------
# a=[i for i in range(10) if i%2==0]
# print(a)                  

# #------------------------------------
# # Python program to print duplicates from 
# # a list of integers
# lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

# uniqueList = []
# duplicateList = []

# for i in lis:
# 	if i not in uniqueList:
# 		uniqueList.append(i)
# 	elif i not in duplicateList:
# 		duplicateList.append(i)

# print(duplicateList)

# list=[1,1,12,3,4,5,5]
# uniqueList=[]
# duplicateList=[]
# for i in list:
#     if i not in uniqueList:
#         uniqueList.append(i)
#     elif i not in duplicateList:
#         duplicateList.append(i)
# print(duplicateList)
# print(uniqueList)       

# #---------maximum or minimum of to number----
# # Python program to find the
# # maximum of two numbers


# def maximum(a, b):
    
#     if a >= b:
#         return a
#     else:
#         return b
    
# # Driver code
# a = 2
# b = 4
# print(maximum(a, b))

# #check the element in list
# # initializing a string
# word = 'find me if you can'
# # using string find() method
# print(word.find('me'))



# lst=[ 1, 6, 3, 5, 3, 4 ] 
# #checking if element 7 is present
# # in the given list or not
# i=7 
# # if element present then return
# # exist otherwise not exist
# if i in lst: 
#     print("exist") 
# else: 
#     print("not exist")
    
# #----------------------------sum and average of list
# # Python program to find the sum
# # and average of the list

# L = [4, 5, 1, 2, 9, 7, 10, 8]


# # variable to store the sum of
# # the list
# count = 0

# # Finding the sum
# for i in L:
# 	count += i

# # divide the total elements by
# # number of elements
# avg = count/len(L)

# print("sum = ", count)
# print("average = ", avg)

# #---------------------------------------------------------/
# a=input('eyn')
# b=0
# for i in range(len(a)):
#     b=b+int(a[i])
# print(b)    

# #---------------------------------------------------------
# a={
#     '1':
#         'name:brij mohan' '\n'
#         'class:12' '\n'
#         'roll no: 1' '\n'
#      ,
#      '2':
#         'name: raju' '\n'
#         'class:12' '\n'
#         'roll no : 2' '\n'
        
            
    
# }    
# b=0
# while b<3:
#     user_input= input('enter the rollno:')
    
#     if user_input in a:
#         print(a.get(user_input))
#     b=b+1    
    
# #------------------------------------------------------
# amount=int(input('eyn'))
# percent=int(input('eyn'))
# percentage=amount/100*percent
# add=amount+percentage
# print(percentage)
# print(f"your amount is {amount} and gst {percent} percent and total amount{add} with gst")


from ty import y


print(y.am)