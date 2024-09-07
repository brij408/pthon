# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
    
    newList[0], newList[-1] = newList[-1], newList[0]

    return newList
    
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))


# # def swaplist(newlist):
    
# # #     newlist[0],newlist[-1]=newlist[-1],newlist[0]
# # #     return newlist


# # # newlist=[1,2,3,4,5]
# # # print(swaplist(newlist))


# # # # Python3 program to swap first
# # # # and last element of a list

# # # # Swap function
# # # def swapList(newList):
# # #     size = len(newList)
    
# # #     # Swapping 
# # #     temp = newList[0]
# # #     newList[0] = newList[size - 1]
# # #     newList[size - 1] = temp
    
# # #     return newList
    
# # # # Driver code
# # # newList = [12, 35, 9, 56, 24]

# # # print(swapList(newList))




# # # def swaplist(newlist):
# # #     size=len(newlist)
    
    
# # #     temp=newlist[0]
# # #     newlist[0]=newlist[size-1]
# # #     newlist[size-1]=temp
    
# # #     return newlist

# # # newlist=[1,2,3,4,5,6]
# # # print(swaplist(newlist))



# # # # Python3 program to swap elements
# # # # at given positions

# # # # Swap function
# # # def swapPositions(list, pos1, pos2):
	
# # # 	list[pos1], list[pos2] = list[pos2], list[pos1]
# # # 	return list

# # # # Driver function
# # # List = [23, 65, 19, 90]
# # # pos1, pos2 = 1, 3

# # # print(swapPositions(List, pos1-1, pos2-1))



# # def swapposition(list):
    
# #     list[pos1],list[pos2] = list[pos2],list[pos1]
# #     return list

# # list=[1,2,3,4,5]
# # pos1,pos2=1,3
# # print(swapposition(list))


# # # Python3 program to swap elements at
# # # given positions

# # # Swap function
# # def swapPositions(list, pos1, pos2):

# # 	# Storing the two elements
# # 	# as a pair in a tuple variable get
# # 	get = list[pos1], list[pos2]
	
# # 	# unpacking those elements
# # 	list[pos2], list[pos1] = get
	
# # 	return list

# # # Driver Code
# # List = [23, 65, 19, 90]

# # pos1, pos2 = 1, 3
# # print(swapPositions(List, pos1-1, pos2-1))

# # #-----------------------------------------------------------------------------------------------------------


def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

# Test the function
word = "madam"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
    
    
def is_palindrome(string):
    reversed_string=string[::-1]
    return string==reversed_string

word='madam'
if is_palindrome(word):
    print(f"{word} is palindrome")
else:
    print(f"{word} is not a palindrome")
    
    
    
# # #--------------------------------- factorial----------------------------------------------------
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# # Test the function
# number = 5
# result = factorial(number)
# print(f"The factorial of {number} is {result}")




# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# number=5
# result= factorial(number)
# print(f"factorial of {number} is {result}")    



#---------------find largest number in------------
def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Test the function
nums = [10, 5, 8, 20, 3]
largest_num = find_largest(nums)
print(f"The largest number is {largest_num}")




def find_largest(number):
    largest=number[0]
    for num in number:
        if num > largest:
            largest=num
            
            
    return largest
nums=[3,5,88,9,5]
largest_num= find_largest(nums) 
print(f" The largest number is{largest_num}")       
            




def find_largest(number):
    largest=number[0]
    for num in number:
        if num>largest:
            largest=num
            
            return largest
nums=[22,33,44,6,7]
lartgestnumber=find_largest(nums)
print(f"the largest number is {lartgestnumber}")        
    
    
# # #-----------------reverse string------------------------------------
# # def reverse_string(string):
# #     return string[::-1]

# # # Test the function
# # text = "Hello, World!"
# # reversed_text = reverse_string(text)
# # print(reversed_text)





# # def reverse_string(string):
# #     return string[::-1]

# # text='hello'
# # reverse=reverse_string(text)
# # print(f"the reverse string is{reverse}")

# # #--------------------find a frequency of list________________

# # # def count_frequency(numbers):
# # #     frequency = {}
# # #     for num in numbers:
# # #         if num in frequency:
# # #             frequency[num] += 1
# # #         else:
# # #             frequency[num] = 1
# # #     return frequency

# # # # Test the function
# # # nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
# # # frequency_count = count_frequency(nums)
# # # print(frequency_count)




# # # def count_frequency(numbers):
# # #     frequency={}
# # #     for num in numbers:
# # #         if num in frequency:
# # #             frequency[num]+=1
# # #         else:
# # #             frequency[num]=1
# # #     return frequency

# # # nums=[1,1,1,2,2,3,3,3,3,3,]        
# # # frequency_count=count_frequency(nums)
# # # print(frequency_count)
            
         

# # # def frequency_count(numbers):
# # #     frequency={}
# # #     for num in numbers:
# # #         if num in frequency:
# # #             frequency[num]+=1
# # #         else:
# # #             frequency[num]=1
            
# # #     return frequency   
# # # nums=[1,1,1,1,2,2,2,4,4,4,5]
# # # count_frequency=frequency_count(nums)
# # # print(count_frequency)
 
 
 
# # #-------------------------number is prime or not--------
# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# # Test the function
# num = 17
# if is_prime(num):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

            


# # #-----------------------common element in twolist________
# # # def find_common_elements(list1, list2):
# # #     common_elements = []
# # #     for item in list1:
# # #         if item in list2:
# # #             common_elements.append(item)
# # #     return common_elements

# # # # Test the function
# # # list_a = [1, 2, 3, 4, 5]
# # # list_b = [4, 5, 6, 7, 8]
# # # common = find_common_elements(list_a, list_b)
# # # print(common)

# # # def find_common_element(list1,list2):
# # #     common_element=[]
# # #     for item in list1:
# # #         if item in list2:
            
# # #             common_element.append(item)
# # #     return common_element

# # # list1 =[1,2,3,4,5,6]
# # # list2=[1,2,3,4,59,0]
# # # common=find_common_element(list1,list2)
# # # print(common)


# # def find_common_element(list1,list2):
# #     common_element=[]
# #     for num in list1:
# #         if num in list2:
# #             common_element.append(num)
# #     return common_element

# # list1=[1,2,3,4,5]
# # list2=[2,3,4]
# # common=find_common_element(list1,list2)
# # print(common)
        
        
        
# # #-----------------------bubble sort_____________
# # def bubble_sort(elements):
# #     
# # for i in range(len(a)):
# #     x=a[i]
# #     for j in range(len(a)):
# #         y=a[j]
# #         if a[i]<a[j]:
# #             c=a[i]
# #             a[i]=a[j]
# #             a[j]=c
# # # Test the function
# # nums = [5, 2, 8, 1, 9]
# # bubble_sort(nums)
# # print(nums)        


# def  bubble_sort(a):
     
#     for i in range(len(a)):
#          x=a[i]
#          for j in range(len(a)):
#               y=a[j]
#               if x<y:
#                 c=a[i]
#                 a[i]=a[j]
#                 a[j]=c
                  
#     return a
            
# # Test the function
# nums = [5, 2, 8, 1, 9]
# bubble_sort(nums)
# print(nums)        

# # #----------------------find second largest number_______
# def find_second_largest(numbers):
#     largest = float('-inf')
#     second_largest = float('-inf')
#     for num in numbers:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num > second_largest and num != largest:
#             second_largest = num
#     return second_largest

# # Test the function
# nums = [10, 5, 8, 20, 3]
# second_largest_num = find_second_largest(nums)
# print(f"The second largest number is {second_largest_num}")



# # second method

# def findsecondlargestnumber(number):
#     a = number.sort()
#     b =number[-2]
#     return b
    
# nums = [1,2,3,4,5,6]
# secondlargestnumber=findsecondlargestnumber(nums)
# print(secondlargestnumber)



# # #---------------------------------write a program to remove duplicates from a list  -------
# # def remove_duplicates(numbers):
# #     unique_numbers = []
# #     for num in numbers:
# #         if num not in unique_numbers:
# #             unique_numbers.append(num)
# #     return unique_numbers

# # # Test the function
# # nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
# # unique_nums = remove_duplicates(nums)
# # print(unique_nums)



# def remove_duplicate(numbers):
#     unique_number=[]
#     for num in numbers:
#         if num not in unique_number:
#             unique_number.append(num)
#     return unique_number

# list=[1,1,2,3,4,4,5,5,6]
# unique=remove_duplicate(list)
# print(unique)        








# a =4

# check = False
# for i in range(2,a):
    
#     if a % i ==0:
#         check = True
        
        
# if check  or a == 1:
#     print('nota prime number')
# else:
#     print('prime number')
    
# #--------------------------------------------------
# # Python Program to find sum
# # of nested list using Recursion

# def sum_nestedlist( l ):
	
# 	total = 0
# 	for j in range(len(l)):
	
# 		if type(l[j]) == list :
			
# 			total+= sum_nestedlist(l[j])
# 		else:
# 			total += l[j] 
			
# 	return total
			
# print(sum_nestedlist([[1,2,3],[4,[5,6]],7]))

# # def sum_nestedlist(l):
    
# #     total=0
# #     for i in range(len(l)):
# #         if type (l[i]) == list :
# #             total+= sum_nestedlist(l[i])
# #         else:
# #             total +=l[i]
# #     return total
# # print(sum_nestedlist([[1,2,3],[4,[5,6]],7]))        

# def sum_nestedlist(l):
    
#     total=0
#     for i in range(len(l)):
#         if type == list:
#             total+=sum_nestedlist(l[i])
#         else:
#             total+=l[i]
#     return total
# print(sum_nestedlist([[1,2,3],[4,[5,6]],7]))            

# #------------------------------------------------------------------------
# # Python program to remove empty tuples from a
# # list of tuples function to remove empty tuples
# # using len()


# # def Remove(tuples):
# # 	for i in tuples:
# # 		if(len(i) == 0):
# # 			tuples.remove(i)
# # 	return tuples


# # # Driver Code
# # tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
# # 		('krishna', 'akbar', '45'), ('', ''), ()]
# # print(Remove(tuples))


# def remove(tuple):
#     for i in tuple:
#         if (len(i)==0):
#             tuple.remove(i)
#     return tuple

# tuple =[(),('1','2','3'),(),('4')]
# print(remove(tuple))


# #----------------------------------------------------
# # Python program to print all 
# # the possible combinations 

# def comb(L): 
	
# 	for i in range(3): 
# 		for j in range(3): 
# 			for k in range(3): 
				
# 				# check if the indexes are not 
# 				# same 
# 				if (i!=j and j!=k and i!=k): 
# 					print(L[i], L[j], L[k]) 
					
# # Driver Code 
# comb([1, 2, 3])



# def comb(l):
#     for i in range(3):
#         for j in range(3):
#             for k in range(3):
                
#                 if (i!=j and j!=k and k!=i):
#                     print(l[i],l[j],l[k])
# comb([1,2,3])                

# #----------------check the string is anagram or not------------------


def check(s1, s2):
    
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
        
s1 = input("Enter string1: ")
# input1: "listen"
s2 = input("Enter string2: ")
# input2: "silent"
check(s1, s2)
# Output: the strings are anagrams.


# def check(s1,s2):
#     if (sorted(s1)==sorted(s2)):
#         print("the string are anagrams.")
#     else:
#         print("the string aren't anagram.")
        
# s1= input('enter the string')
# s2=input('enter the number')        
# check(s1,s2)