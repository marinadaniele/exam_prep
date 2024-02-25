# import random
# lives = 3
#
# while lives:
#     print("You have", lives, "lives left")
#     dice_roll = random.randint(1,6)
#     if dice_roll == 6:
#         print("You rolled a 6, you win!!!")
#         break
#     else:
#         print("You rolled a", dice_roll, "try again")
#         lives = lives - 1 #or "lives -=1"

# if lives == 0:
#     print("You lost all your lives, game over")

# else
#   print("You lost all your lives, game over")

############################################################# infinite while loop
#
# x = 0
#
# while True:
#     print(x)
#     x += 1
#
# ############################################################### while loop
#
# x = 0
#
# while x < 10:
#     print(x)
#     x += 1

####################################################################

# name = input("Enter your name: ")
#
# if name == "":
#     print("You did not enter your name, please enter your name")
# else:
#     print("Hello ", name)

###################################################################
# but if you want to continually prompt user
#
# name = input("Enter your name: ")
#
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
# print("Hello ", name)
#
# age = int(input("Enter your age"))
#
# while age <= 0:
#     print("Age can't be zero or negative")
#     age = int(input("Enter your age"))
#
# print("You are", age, "years old")


#############################################################################
# QUESTIONS ON SLIDES

# Print the multiplication table 1-10 without duplicates (if a*b=c appears, then b*a=c should not)
for i in range(1, 11):
    for j in range(i, 11):
        print(f"{i} * {j} = {i*j}")

# Suppose you can only do additions. Write a program that reads two positive, integer numbers a and b. It computes a**b.









