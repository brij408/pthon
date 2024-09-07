# def add(a,b):
#     print(a+b)
    
# add(10,30)
# add(600,3)
# add(40,45)

# # funtion without parameter
                   
    


#     #type of parameter
#     #1 positional
    
# def add(a=3,b=5,c=1):
#     print(a+c)
    
    
    
# add(3,1)


# #2 key words
 

# def dis(name,age,lastname):
#     print(f"my name is{name} {lastname} and age is {age}")
    
# # dis('ritik','sharma','age')    
# dis(age='24',name='ritik',lastname='sharma')


# #3default
# def add (a=0,b=0,c=0):
#     print(a+b+c)
    
# add(1,2)    
    
    
# #4(*args)

# def add(*args):
#     c=0
#     for i in args:
#         c=c+i
#         print(c)
# add(1,3,3,4,5,6,7,8)        
    
# #5 (**kwargs)
# def add(**kwargs):
#     a=kwargs['name']
#     b=kwargs['last']
#     c=a+b
#     print(c)
    
# add(name='ritik', age ='24',last='sharma')    
    
# #local and globale variable

# a=0
# def add():
#     globals 
#     a=5
#     print(a)

# print(a) 
# add()
# print(a)
    
# # nested funtion

# def add():
#     print('brij')
#     def inner():
#         print('im nested funtion')
#     inner()    
# print('hello')
# add()      

# #what is return 
# def add():
#     return 24

# b= add()


# #-----------------

# def add (a,b):
#     c=a+b
#     return c
# x=add(2,4)
# y=add(9,1)
# print(y)

# #funtion return another funtion
# def add():
#     print('add')
#     return second()

# def second():
#     print('my name is second')
#     return 24

# x=add()
# y=second()
# print(x)
# print(y)

# # funtion pass as a argument

# def add(a):
#     b=a()+10
#     print(b)
# def seven():
#     return 7
# add(seven) 


# #lamda

# def add(a,b):
#     print(a+b)
    
    
# #------------------
# add =lambda a,b:a+b
# b=add(2,3)
# print(b)
    
# #recurssion
# a=0
# def add():
    
#     globals 
#     a=5
#     a=a+1
#     print(a)
#     return add()

# print(a)
# add()

# #-------------------------------------------------------------------------------------
    
# def sol(l):
#     b =  []
#     for i in l:
#         if isinstance(i,list):
#             b.extend(sol(i))
#         else:
#             b.append(i)
            
#     return b
    
# # v = [1,2,[3,4,[5,6,7,[8,9,10,[1,2,[3,5,8,[5]]]]],1,2,[3,4,[5,6,7,[8,9,10,[1,2,[3,5,8,[5]]]]]]], 1,2,[3,4,[5,6,7,[8,9,10,[1,2,[3,5,8,[5]]]]]]]   
# b = sol([[1,2,2], [2,5,6]])


# print(b)

# #-----------------------------------------------------------------------------------------------------

# def sol(l):
#     b =  []
#     for i in l:
#         if isinstance(i,list):
#             b.extend(sol(i))
#         else:
#             b.append(i)
            
#     return b
    
# v = [1,2,[3,4,[3]]]   
# b = sol(v)


# print(b)


# #------------------------------------------------------------------------------------------------------------------


  
# def b(func):
#     def inner(a,b):
#         print(a+b)
#     return inner
     
     
# @b    
# def a(a,b):
#     print('brij')
# c=a(1,2)




am =  'p'