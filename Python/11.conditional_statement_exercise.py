"""
Exercise - 1
Find the min of 3 given numbers
"""

"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1<num2 and num1<num3:
    print("Minimum number is: ", num1)

elif num2<num1 and num2<num3:
    print("Minimum number is: ", num2)

else: 
    print("Minimum number is: ", num3)

    
"""


"""
Exercise - 2
ATM Machine menu

1. Pin change 
2. balance check
3. withdraw 
4. Deposit
5. Exit
"""

menu = input("""
Hi there! Welcome to ATM
Please choose,

1. Enter 1 for Pin change
2. Enter 2 for Balance check
3. Enter 3 for Withdraw
4. Enter 4 for Deposit
5. Enter 5 for Exit
         
""")

# print(menu)


if menu == "1":
    print("Pin change")

elif menu == "2":
    print("Balance check")

elif menu == "3":
    print("Withdraw")

elif menu == "4":
    print("Deposit")

else:
    print("Exit")
