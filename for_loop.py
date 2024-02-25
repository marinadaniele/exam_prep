nums = [1, 2, 3, 4, 5]
#
# for num in nums:
#     if num == 3:
#         print("Found!")
#         continue
#     print(num)

############################################ Loop in a loop
#
# for num in nums:
#     for letter in 'abc':
#         print(num, letter)
#
# ############################################# running a loop only a specific amount of times
# ######## RANGE
#
# for i in range(1,11):
#     print(i)
#
# for x in reversed(range(1, 11, 3)):
#     print(x)
#
# print ("Happy new year")

# reversed = counts down from 10
# step = Adding a third value which indicates by how much to count

################################################################### no 13 for bad luck
# for x in range(1, 21):
#     if x == 13:
#         continue
#     else:
#         print(x)

###################################################################
# result = 0
# for i in range(0,10):
#     result += i
#     print("The sum of the first 9 numbers is", result)
#
# result = 0
# text = "1234567890"
# for i in text:
#     result += int(i)
#     print("The sum of the first 9 numbers is", result)


######################################################################

##class exercises on slides
#
# divisor = 3
# for num in range(0, 12, 3):
#     print(num/divisor)
#
# for letter in 'Ahola':
#     print(letter)
#
# num = 0
# while num <= 5:
#     print(num)
#     num += 2
# print("Out")
# print(num)

########################################################################## infinite loop
# num = 0
# count = 0
# while num <= 19:
#     if num % 3 == 0:
#         count += 1
#         num + 1
#         print("Numbers divisible by 3", count)

