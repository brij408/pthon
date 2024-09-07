# class Calculator(object):
    
#     def add(self,a,b):
#         print(a+b)
#     def divide(self,a,b):
#         print(a /b)
#     def multiply(self,a,b):
#         print(a*b)
#     def subtraction(self,a,b):
#         print(a-b)    

# a=Calculator()
# a.add(2,7)     

# b=Calculator()
# b.add(2,3)   
                
                
                
                
                
                
                
# #inheritence
# # simple or single inheritence

# class parent:
#     def property(self):
#         print('1cr')
        
# class child(parent):
#     def dis(self):
#         print('brij')

# b=child()
# b.property()                               


#multilevel

# class Gparent:
#     def property(self):
#         print('1cr')
# class parent(Gparent):
#     def name(self):
#         print('raj')
        
# class child(parent):
#     def indo(self):
#         print('my name is xyz')

# a=child()
# a.property()
# a.name()
# a.indo()
                        
# #hererical inheritence
# class father:
#     def property(self):
#         print('1cr')
# class son(father):
#     def name(self):
#         print('son')
# class daughter(father):
#     def same(self):
#         print('daughter')
        
        
# a=son()
# a.property()
# b=daughter()
# b.property()        
                
          
# class father:
#     def name(self):
#         print('coco')    
# class mother:
#     def coca(self):
#         print('country')  
# class son(father ,mother):
#     def sf(self):
#         print('soso')     
        
# a=son()
# a.coca()
# a.name()
                      



#static method

# class student:
#     grade =4
    
#     def __init__(self,name ,age):
#         self .name =name
#         self.age =age
        
#     def get_data(self):
#         print({'name': self.name,'age':self.age,'grade':self.grade})
        
#     @classmethod
#     def update_grade(cls,grade):
#         cls.grade =grade    
#     @staticmethod    
#     def check_age(age):
#         if age>18:
#             print('above 18')
#         else:
#             print('below 18')    
        
        
        
# s1=student('abc',45)
# s2=student('xyz',32)   

# student.update_grade(20)
# student.check_age(17)


# s1.get_data()
# s2.get_data()         
        
    
# #access specifier
# class salary:
#     brijsalary="12lakh"
#     _rajsalary="25l"
#     __ramosalary="24l"
#     def sal(salary):
#         print('ya')
      
      
# a=salary()
# print(a.brijsalary) 
# print(a.__ramosalary) 
# print(a._rajsalary)
      
   
#private
class Employee:
    def __init__(self) :
        self.__name='brij'
        
a=Employee()
# print(a.__name)#cannot be accessed directly   
print(a._Employee__name)#can be accessed indirectly   #name mangling
# print(a.__dir__())   


#protected
     
            
    