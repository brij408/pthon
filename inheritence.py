# class Employee:
#     def __init__(self ,name,id) :
#         self.name= name
#         self.id =id
        
        
#     def showdetails(self):
#         print(f"the name of employee:{self.id} is {self.name}")
        
# class programmer(Employee):
#     def show(self):
#         print('the default langauge is python')        
        
        
        
        
# e1=Employee('rohan das', 420)
# e1.showdetails()            
        
# e2=programmer('rohan das', 4299)
# e2.showdetails()
# e2.show()





# #mutiple inheritence


# class Employee:
#     def __init__(self,name):
#         self .name=name
        
#     def show(self):
#         print(f"the name is{self.name}")    
    
# class Dancer:
#     def __init__(self,dance):
#         self.dance=dance
        
#     def show(self):
#         print(f"the name is{self.dance}")    
        
        
# class DancerEmployee(Dancer,Employee):
#     def __init__(self,dance, name):
#         self.dance=dance
#         self.name =name


# o =DancerEmployee('kathak','shivani')
# print(o.name) 
# print(o.dance)        
# o.show()        

# #multilevel inheritence

# class Animal:
#     def __init__(self,name, species):
#         self.name=name
#         self.species=species
        
#     def show_details(self):
#         print(f"name:{self.name}")
#         print(f"species:{self.species}")
        
# class Dog(Animal):
#     def __init__(self, name, bread):
#         Animal.__init__(self,name,species="Dog")
#         self. bread=bread
        
#     def show_details(self):
#         Animal.show_details(self) 
#         print(f"bread:{self.bread}")
        
# class Goldenretriver(Dog):
#     def __init__(self, name, color):
#         Dog.__init__(self,name,bread="Golden retriver")
#         self.color=color
        
#     def show_details(self):
#         Dog.show_details(self)
#         print(f"color:{self.color}")
        
# o=Goldenretriver("tommy0","black")
# o.show_details(
    
# )            


#-------------------------------------------------------------------------
# class A:
#     def sort(self,a):
#         for i in range(len(a)):
#             x=a[i]
#             for j in range(len(a)):
#                 y=a[j]
#                 if x<y:
#                     c=a[i]
#                     a[i]=a[j]
#                     a[j]=c
#         return a     
# class B:
#     def removeduplicate(self,b):
#         c=[]
#         for i in range(len(b)):
#             if i not in c:
#                 c.append(i)
#         return c   
# class C(A,B):  
#     def sf(self):
#         pass
        
        
# list1=[1,5,43,2]    
# list2=[1,1,2,4,]
# o=C()
# z=o.removeduplicate(list2)
# print(z)
# s=o.sort(list1)
# print(s)
        
# class A:
#     c="yo yo"
#     @classmethod
#     def display(cls):
#         print(cls.c)
#         pass
         
# x=A()
# x.display()  
# print(x)        
   
   
#super()
class Empoloyee:
    
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
class programmer(Empoloyee):
    def __init__(self, name, id,lang):
        super().__init__(name ,id)
        self.lang=lang
        
rohan =Empoloyee('rohan das','420')
harry =programmer('harry','2345','python')
print(harry.name)
print(harry.id)
print(harry.lang)                