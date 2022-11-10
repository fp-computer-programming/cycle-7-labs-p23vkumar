#1. Create a Python file named lab_6-8
#2. Create a program that asks a user to input 3 numeric values

#create input variables for all of them
Num1 = input("Enter Number: ")
#create input variables for all of them
Num2 = input("Enter Number: ")
#create input variables for all of them
Num3 = input("Enter Number: ")

#3. Construct a list of the 3 input values, in the order that the user gave them

#create a list of the numbered vlaues
N_U_M_B_E_R_L_I_S_T = [Num1, Num2, Num3]

#4. Have the program display the string “even” if all numbers in the list are even.

#create input variables for all of them
Number1 = int(Num1)
#create input variables for all of them
Number2 = int(Num2)
#create input variables for all of them
Number3 = int(Num3)

if Number1%2 == 0 and Number2%2 == 0 and Number3%2 == 0:
    print("List of Numbers is Even")
elif Number1%2 != 0 and Number2%2 != 0 and Number3%2 != 0:
    print("List of numbers is odd")
else:
    print("List of numbers is Mixed")
#5. Have the program display the string “odd” if all numbers in the list are odd.
#6. Have the program display the string “mixed” if the numbers in the list are both even and odd.
#• You may assume accurate input values. You may NOT use a loop.