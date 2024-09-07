# # a={
# #     'ramesh':70,
# #     'sham':50,
# #     'ramo':50,
# #     'kamo':70
# # }
# # b=list(a.values())
# # c=[]
# # d=0
# # for i in range(len(a)):
# #     if b[i] not in c:
# #         c.append(b[i])
# #     else:
# #         d=d+b[i]
# #         print(b[i],'is duplicate')
# # print(d)   
             
# # a=[1,1,2,2,3,4,5]
# # b=[]
# # c=[]
# # for i in range(len(a)):
# #     if a[i] not in b :
# #         b.append(a[i])
# #     else:
# #         c.append(a[i])

# # print(c)

            
          
# # a=[i for i in  range (1,100+1) if i%2==0]
# # print(a)
            
            
# # a=[9,8,7,6,5,4,3,2]
# # for i in range(len(a)):
# #     x=a[i]
# #     for j in range(len(a)):
# #         y=a[j]
# #         if x<y:
# #             c=a[i]
# #             a[i]=a[j]
# #             a[j]=c
# # print(a)            

# # a=[[9,8,7],[6,5,4,3,2]]
# # for k in a:
# #      for i in range(len(k)):
# #           x=k[i]
# #           for j in range(len(k)):
# #                y=k[j]
               
# #                if x<y:
# #                 c=k[i]
# #                 k[i]=k[j]
# #                 k[j]=c
# # print(a)        



# # a=(1,2,3,4)
# # b=list(a)
# # b.append(5)
# # c=tuple(b)
# # print(c)



# # a=[1,-2,-3,4]
# # pos_count,neg_count=0,0
# # for i in a:
# #     if i>0:
# #         pos_count+=1
# #     else:
# #         neg_count+=1
# # print(pos_count,'is positive')
# # print(neg_count,'is negitive')
        
    


# # a=[1,-2,-3,4]
# # pos_count,neg_count=0,0
# # for i in a:
# #     if i<=0:
# #         pos_count+=1
# #     else:
# #         neg_count+=1
# # print(pos_count,'is positived')  
# # print(neg_count,'is negitive')      

#
# # a= input('enter the number')
# # b=int(a)

# # x=1
# # for i in range(1,b+1):
# #     x=x*i
# # print(x)

# # a=input('eyn')
# # b=0
# # for i in range(len(a)):
# #     b=b+int(a[i])
# # print(b)    
    
    
    
# # a={
# #     'ramo':0,
# #     'sham':3,
# #     'pamo':3


# # }    
# # c=0
# # for i  in a:
# #     c=c+a[i]
# # print(c)    


# #--------------------------------------------------------------

# a={
#     'apple':'20',
#     'banana':'30',
#     'mango':'30'
# }

# b= input('enter your key or value')
# key_list =list(a.keys())
# value_list=list(a.values())
 
# if b in key_list:
#     print('yes')
#     index=key_list.index(b)
#     print(value_list[index])
    
    
# elif b in value_list:
#     print('yes')
#     index= value_list.index(b)
#     print(key_list[index])
    
    
# else:
#     print('no')    




# # a={
# #     'apple':'20',
# #     'banana':'30',
# #     'orange':'40'
# # }

# # b=input('enter your key or value')
# # key_list=list(a.keys())
# # value_list=list(a.values())

# # if b in key_list:
# #     print('yes')
# #     index=key_list.index(b)
# #     print(value_list[index])
    
    
# # elif b in value_list:
# #     print('yes')
# #     index=value_list.index(b)
# #     print(key_list[index])
    
# # else:
# #     print('no')



# # a={
# #     'apple':'20',
# #     'banana':'30',
# #     'mango':'30'
# # }
# # user_input=input('enter the key:')
# # if user_input in a:
# #     print('yes we have:',a.get(user_input))
    
# # else:
# #     new_val=input('we dont have this item plzz enter the value')
# #     a.update({user_input:new_val})
    
# # print(a)    
    
    
    
# a={
#       '101':20,
#       '102':30,
#       '103':30,
#       '104':50   
      
#   }
# c=0
# for i in a:
#     c+=a[i]
# print(c)      
      
      
      
      

# a={
#     '101':{
#             'name':'cold drink',
#             'price':20
#           },
#     '102':{'name':'sugar',
#            'price':200
        
#           }
    
# }

# print(a.get('price')+a.get('102').get('price'))




a={
    'sugar':50,
    'rice':50,
    'wheat':60,
    'salt':60,
    'macroni':70
}    

d=list(a.values())
l={}
for i in range(len(d)):
    n=d[i]
    m=d.count(d[i])
    k=l.setdefault(d[i],m)
print(l)    
