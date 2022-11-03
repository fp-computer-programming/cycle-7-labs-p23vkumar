#1. Create a Python file named lab_6-1.py
#2. Create a array that contains the numbers 1 to 5 store it as a variable called my_arr.

#array of a list of numbers 1-5 in a list
#defined variable as my_arr
my_arr = ['1', '2', '3', '4', '5']
print(my_arr) #print variable my_arr

#3. Write a statement using the indexing operator that prints the number 3 in my_arr.

#variable x1 = the index of my_arr to print 3
x1 = my_arr[2] 
#print x1 or the variable
print(x1)

#4. Write a statement that prints the length of my_arr.

#x2 (variable) = the length of the list
x2 = len(my_arr)
#print variable
print(x2)

#5. Write a statement that repeats my_arr 3 times.

x3 = (my_arr) * 3
print(x3)

#6. Write a statement that converts "string" to an array.

#define convert arry variable to equal string
ConVert_Array = "SpaceX"
#print variable as a list to convert it to a array
print(list(ConVert_Array))