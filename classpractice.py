# class student:
#     name ='brij'
    
# s1=student()
# print(s1.name)        

# s2=student()
# print(s2.name)


# class car:
#     color ='blue'
#     brand='BMW'

# car1=car()

# print(car1.color)    


# #constructor
# class student:
    
#     college_name='abc college' # class attribute
#     #default construtor
#     # def__init__(self):
#     #     pass
#     #parameterised constructor
#     def __init__(self,fullname): #(self ,name ,marks) bhi ker skte te hai
#         self.name =fullname   #name and marks are variable or attributes # obj attribute
#         #self.marks=marks
#         print('adding new student in database..')
        
        
# s1=student('brij') 
# print(s1.name )       #(s1.name ,s1marks)

# print(student.college_name)

# s2=student('rana') 
# print(s2.name)       






#---------------------------------method
class student:
    college_name='abc college'
    def __int__(self,name, marks):
        
        self.name= name
        self.marks=marks
        
        
    def welcome(self):
        print('welcome student',self.name)  
        
        
        
    def get_marks(self):
        return self.marks    
        
s1=student('brij',97)
s1.welcome()
print(s1.get_marks)          
    


#practice question ___________________
#create student class that takes name& marks of 3subjects as aruguments in constructor .
#then create a methods to print the average.


class student:
    def __init__(self, name ,marks):
        self. name = name
        self .marks=marks
    def get_avg(self):
        sum =0
        for val in marks:
            summ+=val
            print('hi',self.name,'your avg is',sum/3)
                
        
s1 =student('tony stark',[ 98,95,96])   
s1.name='ironman'
s1.get_avg() 



