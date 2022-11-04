#1. Create a Python file named lab_6-2.py
#2. Create a variable my_row and set it equal to a list that 
#contains the names of 2 people in your row.

#create variable of my_row for list
my_row = ['Brian', 'Jan']
print(my_row)

#3. Using slices, add your name to the end of the list.

#index the list of my_row and set it equal to string
my_row[1] = 'Vishnu'
#print new variable
print(my_row)

#4. Create another variable my_row2 and set it equal to my_row.

my_row2 = my_row

#5. Add a statement that prints my_row2

print(my_row2)

#6. Add a statement that removes the value at index 1 from my_row

del my_row[0]

#7. Add a statement that prints my_row. What do you notice happens 
#and why?

print(my_row)
print("I notice that the name is Brian is gone and my name is only there because as Defined by the del statement, I deleted the first value of the index and it deleted it, leaving only my name left")