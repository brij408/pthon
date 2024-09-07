# def func(brij):
#     def luka(a,b):
#         print(a+b)
#     return luka
# @func
# def inner(a,b):
#     print('yes ')
# inner(2,7)    



# def sol(l):
    
#     b=[]
#     for i in l:
        
#         if isinstance(i,list):
#             b.extend(sol(i))
#         else:
#             b.append(i)
#     return b
# v=[1,2,3,[2,3,4,5,[1,3,4,[1,2,3]]]]
# b=sol(v)
# print(b)       
    

# def sol(p):
#     b=0
#     for i in range(len(p)):
#         if  type(p[i])==list:
#             b+=sol(p[i])
#         else:
#             b+=p[i]
#     return b
# v=[1,2,3,[2,3,4,5,[1,3,4,[1,2,3]]]]    
# c=sol(v)
# print(c)   



# def  find_frequency(number):
    
#     frequency={}
#     for num in number:
#         if num in frequency:
#             frequency[num]+=1
#         else:
#             frequency[num]=1
#     return frequency

# b=[1,1,1,3,3,4,5,6]   
# c=find_frequency(b)   
# print(c)  


# b=[[1,2,3,4,5],set(),1,2,34,4]
# a=0
# while True:
#     x=True
#     for i in b:
        
#         if isinstance(i,list):
#             x=False
#         elif isinstance(i,set):
#             x=False
#     if x:
#         break
#     if isinstance(b[a],list):
#         b.remove(b[a])
#         continue
#     elif isinstance(b[a],set):
#         b.remove(b[a])
#         continue
# a=a+1
# print(b)        
            
            
# #*args

# def luka(*args):
#     print(a+b+c)
    
# luka(1,2,3,5,7)    
    
    
#**kwargs    
def luka(**kwargs):
    res=kwargs['n']*kwargs['m']
    print(res)
    return 
luka(a=1,b=2,c=3)

#3default
def add (a=0,b=0,c=0):
    print(a+b+c)
    
add(1,2)    

#2 key words
 

def luka(name,age,lastname):
    print(f"my name is{name} {lastname} and age is {age}")
    
luka(name='rana',age='16',lastname='ran')    





#-----------------------
a={1,2,3,5,6,7,8,}

