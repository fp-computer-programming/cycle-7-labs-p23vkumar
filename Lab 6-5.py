#1. Create a Python file named lab_6-5
#2. Create a program that will take a list (of numbers) of any length and return the highest and lowest value in the list. If the list does not have at least 2 unique numbers, return the string: “error: list does not meet specifications”)

#create a list
x_L_I_S_T = [16, 100, 20, 56, 76]

#print List 
print(x_L_I_S_T)

#reverse list if needed 
x_L_I_S_T.sort (reverse = True)
#print reversed list
print(x_L_I_S_T)

#length of list has to be greater than 2
if len(x_L_I_S_T) > 2:
    #print(higher number)
    print(x_L_I_S_T[0])
    #print(lower number)
    print(x_L_I_S_T[-1])
    #another if conditions for higher not equal to lower
    if x_L_I_S_T[0] != x_L_I_S_T[-1]:
        #print expression to meet command
        print("Meets Speciications")
#otherwise redo it
else:
    print("Error! List Does Not Meet Specifications")
