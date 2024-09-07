a={
    'apple':'20',
    'banana':'30',
    'mango':'30'
}

b= input('enter your key or value')
key_list =list(a.keys())
value_list=list(a.values())
 
if b in key_list:
    print('yes')
    index=key_list.index(b)
    print(value_list[index])
    
    
elif b in value_list:
    index= value_list.index(b)
    print(key_list[index])
    
    
else:
    print('no')    



# a={
#     'apple':'20',
#     'banana':'30',
#     'mango':'30'
# }

# b= input('enter your key or value:')
# key_list =list(a.keys())
# value_list=list(a.values())
 
# if b in key_list:
#     # print('yes')
#     # index=key_list.index(b)
#     # print(value_list[index])

#      print(a.get(b))
    
# elif b in value_list:
#     # index= value_list.index(b)
#     # print(key_list[index])
    
#     print(a.get(b))
    
# else:
#     print('no')   
    
    
    

# a={
#     '101':{
#             'name':'cold drink',
#             'price':20
#           },
#     '102':{'name':'sugar',
#            'price':200
        
#           }
    
# }

# print(a.get('101').get('name'))
# print(a.get('price')+a.get('102').get('price'))



a={
    'apple':'20',
    'banana':'30',
    'mango':'30'
}


user_input =input('enter fruit name')

if user_input in a:
  print('yes we have and price',a.get(user_input))
  
  
else:
  new_val =input('we dont have value plzz enter value')
  a.update({user_input: new_val}) 
  
  
print(a)  




a={
    '101':{
            'name':'cold drink',
            'price':20
          },
    '102':{'name':'sugar',
           'price':200
        
          }
    
}

print(a.get('101').get('price')+a.get('102').get('price'))

    
  
a={
      '101':20,
      '102':30,
      '103':30,
      '104':50   
      
  }
c=0
for i in a:
    c+=a[i]
print(c)      
      
  
 
# a={
#     '101':{
#             'name':'cold drink',
#             'price':20
#           },
#     '102':{'name':'sugar',
#            'price':200
        
#           }                
# }  

# b=input('enter the the number:')                            plus keda kerna 
# print(a.get(b).get('name'))



# a={
#     'remaesh':70,
#     'ganesh':50,
#     'ramo':70,
# }

# b=list(a.values())
# d=0
# c=[]
# for i in range(len(b)):
#     if b[i] not in c:
      
#       c.append(b[i])                               first valuebhi same thi per add ni hui
#     else:
#       d+=b[i]
#       print(b[i],'is dupilcate')
      
# print(d)      
      
      
      
      
#instance method vset remove

# a=[{4,3,2,7,8},[4,3,2,5],{1,2,3,4}]   
# for i in a:                                          
#   if isinstance(i,list):
#     a.remove(i)                                  
#   elif isinstance(i,set):
#     a.remove(i)  
#   elif isinstance(i,set):  
#       a.remove(i) 
    
# print(a)    
    
    
#  #items kine time aayi hai
# a={
#     'sugar':50,
#     'rice':50,
#     'wheat':60,
#     'salt':60,
#     'macroni':70
# }    

# d=list(a.values())
# l={}
# for i in range(len(d)):
#     n=d[i]
#     m=d.count(d[i])
#     k=l.setdefault(d[i],m)
# print(l)    

# mcq test

a={
    '1':{
        'question-1':'who is the president of india',
    
    'option':{
        'a':'narender modi',
        'b':'darupati murmu',
        'c':'amit shah',
        'd':'lalu yadav'
        
    }
        
    },
    'answer':'b',
    
    '2':{
        'question-2':'who is the prime of india',
        
        'option':{
            'a':'lalu yadav',
            'b':'narendre modi',
            'c':'amit shah',
            'd':'raj nath singh'
            
            
            
        }
    },
    'answer':'b',
    
    '3':{
        'question-3':'who is the defence minister of india ',
        
        'option':{
            'a':'anurag thakur',
            'b':'jai ram thakur',
            'c':'raj nath singh',
            'd':'pappu yadav'
            
        }
        
    },
    
    'answer':'c',
}

b=0
total=0
while b<3:
    user_input=input('enter the question')
    if user_input in a:
        print(a.get(user_input))
        new_val=input('choose the correct answer')
        z=a.get(user_input).get('answer')
        if new_val==z:
            print('your answer is correct')
            total=total+1
        else:
            print('your answer is incorrect')
            total=total-0.5
        b=b+1
print(total)            

#add gst of total amount 

amount=int(input('enter the amount'))
percent=int(input('what percent you want of the amount'))
percentage=amount/100*percent
add=amount+percentage
print(percentage)
print(f"your amount is {amount}and you get{add} amount of money with{percent} percent get")


#-------------------------------------------------------------------------------------------------------------

b=[  2,[1,23,5,5,6,],'erer',5545,[],555,set()]   
a = 0
while True:
    x = 1
    for i in b:
        if isinstance(i,list):
            
            x = 0
        elif isinstance(i,set):
            
            x = 0
    if x == 1:
        break
        
    if isinstance(b[a],list):
        b.remove(b[a]) 
        continue
    elif isinstance(b[a],set):
        b.remove(b[a])
        continue
    a =  a+1

  
    
print(b)




#------------------------------------------------------------------------------------------

def sol(l):
    b =  []
    for i in l:
        if isinstance(i,list):
            b.extend(sol(i))
        else:
            b.append(i)
            
    return b
    
v = [1,2,[3,4,[5,6,7,[8,9,10,[1,2,[3,5,8,[5]]]]],1,2,[3,4,[5,6,7,[8,9,10,[1,2,[3,5,8,[5]]]]]]], 1,2,[3,4,[5,6,7,[8,9,10,[1,2,[3,5,8,[5]]]]]]]   
b = sol(v)


print(b)

def func(d):
    d={'a':1 ,'b':2,'c':3}
    for key in d:
        print('key:',key,'value:',d[key])

D={'a':1 ,'b':2,'c':3}
func(D)

#dictionary as kwargssx

def display(**name):
    print(name['fname']+' '+name['mname']+' '+name['lname'])
    
def main():
    
    
    display(fname ='john',
            mname ='f.',
            lname ='kennedy')
    
    
main()        