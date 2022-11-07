#1. Create a Python file named lab_6-3

#2. Create a list of 4 colors and store it as a variable.

Color_list = ['Red', 'Blue', 'Green', 'Yellow']
#print variable
print(Color_list)

#3. Use a method to add 3 more colors to the list in a single statement.

#extend list
Color_list.extend(['Black', 'Purple', 'Orange'])
#print variable
print(Color_list)

#4. Use a different method to add one additional color to the list.

#append list
Color_list.append('Gold')
#print variable       
print(Color_list)

#5. Use a method to insert a new color at index 3.

#insert method of list
Color_list.insert(3, "Indigo")
#print variable
print(Color_list)

#6. Use a method to create a copy of the list

#define new variable to define copy of list
copy_color_list = Color_list[:]
#print variable
print(copy_color_list)

#7. Use a method to remove all the elements from the copy of the list.
#remove method
copy_color_list.remove("Indigo")
#print(variable)
print(copy_color_list)