#######################################################################################
# division game. Exceptions

try:
    num = input("Give me a number")
    num = int(num)
    num2 = input("Give me another number")
    num2 = int(num2)
    result = num / num2
    print("The division result is", result)

except ValueError:(
    print("Please give me a proper number"))
except ZeroDivisionError:(
    print("The second number can not be zero"))

#######################################################################################

# the last except block shouldn't have an exception name
try:
    num = input("Give me a number")
    num = int(num)
    num2 = input("Give me another number")
    num2 = int(num2)
    result = num / num2

except ValueError:
    print("Please give me a proper number")
except ZeroDivisionError:
    print("The second number can not be zero")
except:
    print("Some other exception I did not see coming")
else:
    print("The division result is", result)