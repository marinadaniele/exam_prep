#example of if usage with bool values
#
# # simple If statement
# age = 18
#
# if age>= 18:
#     print("is an adult")
# else:
#     print("is not an adult")

#################################################################################
## simple if statement second example
# if 6 % 2 == 0:
#     print(6, "is an even number")
#     print("Nothing would have been printed if it were odd")
#
#################################################################################
##alternative if statement
# if 6 % 2 == 0:
#     print(6, "is an even number")
#
# else:
#     print(6, "is an odd number")
#
################################################################################
## chained elif statement
#
# x = 10
# y = 8
# z = 10
#
# if x > y:
#     print('x is greater than y')
# elif x < z:
#     print('x is less than z')
# elif 5 > 2:
#     print('5 is greater than 2')
# else:
#     print('if and elif(s) never ran')
#
# #################################################################################
# # chained elif statement 2
# a = 18
# b = 32
#
# if a > b:
#     print(a,">", b)
# elif a < b:
#     print(a, "<", b)
# else:
#     print(a, "=", b)
#
# ####################################################################################
# # chained elif statement 3
# c = 43
# d = 12
# if c == d:
#     print(c, "=", d)
# else:
#     if c < d:
#         print(c, "<", d)
#     else:
#         print(c, ">", d)

########################################################################################
##IF PROBLEM DONE IN CLASS

try:
    gross_salary = float(input("Enter your gross salary:"))
    income_tax_percentage = 0
    children = int(input("Enter the amount of children that you have:"))

    if gross_salary < 1000:
        income_tax_percentage = 10
    elif gross_salary < 2000:
        income_tax_percentage = 12
    elif gross_salary < 4000:
        income_tax_percentage = 14
    else:  # gross_salary >= 4000
        income_tax_percentage = 18

# Calculate the tax cut based on the number of children
    if gross_salary < 2000:
        tax_cut = children * 1  # 1% tax cut for each child
    else:  # gross salary more than 2000
        tax_cut = children * 0.5  # 0.5% tax cut for each child

        # Apply the tax cut to reduce the income tax percentage
        income_tax_percentage -= tax_cut

        # Make sure the income tax percentage doesn't go below zero
        income_tax_percentage = max(income_tax_percentage, 0)

        # Calculate income tax and net salary
        income_tax = (income_tax_percentage / 100) * gross_salary
        net_salary = gross_salary - income_tax

        print("Your net salary is:", net_salary)

except ValueError:
    print("Please enter a valid number for your gross salary and the number of children.")