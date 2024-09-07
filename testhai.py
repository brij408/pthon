
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




a=0 
while True:
    x=True
    for i in  b:
        if isinstance(i,list):
            x=False
        elif isinstance(i,set):
            x=False
    if x:     
        break
    if isinstance(b[a],list):
        b.remove(b[a],list)
        continue
    elif  isinstance(b[a],set):
        b.remove(b[a],set)
        continue
    a=a+1
    print(a)
          
        