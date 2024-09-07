import random
wining_number =random.randint(1,100)
for i in range(1,4):
    guess_number =input("enter your gussing number")
    int_guess_number = int(guess_number)
    if int_guess_number == wining_number:
        print("you win",wining_number)
        break
    else:
        print("your number is wrong plzz")
        if i == 3:
            print("game over",wining_number)


# import random 
# wining_number = random.randint(1,100)
# for i in range(1,4):
#     guess_number = input('enter your gussing number')
#     int_guess_number = int(guess_number)
#     if int_guess_number == wining_number:
#         print('you win',wining_number)
#         break
#     else:
#         print('you win',wining_number)
#         if i == 3:
#             print('game over', wining_number)
 
 