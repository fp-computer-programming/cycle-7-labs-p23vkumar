#1. Create a Python file named lab_6-4
#2. Create a list of 3 subjects that you have studied at Prep and store it
#as a variable.
    
Fairfield_Prep_Subject = ['AP Calculus AB', 'AP Physics 1', 'AP Physics 2,']
#print variable
print(Fairfield_Prep_Subject)

#3. Use a method to add a fourth subject you have studied to the end of the list.

#append the variable Fairfield_Prep_Subject
Fairfield_Prep_Subject.append('Honors Chemistry')
#print variable       
print(Fairfield_Prep_Subject)

#4. Use a method to return the index of one of the subjects in your list.

#define variable to find the index of the originial list
find_subject = Fairfield_Prep_Subject.index('AP Physics 1')
#print variable       
print(find_subject)

#5. Order the subjects alphabetically using a method.

#create a sort statement of the original list
Fairfield_Prep_Subject.sort()
#print Fairfield_Prep_Subject
print(Fairfield_Prep_Subject)

#6. Use a method to make a copy of this list and store it in a different variable.

#new variable for new copy of list
Fairfield_Prep_SubjectX = Fairfield_Prep_Subject[:]
#print new variable
print(Fairfield_Prep_SubjectX)

#7. Use a method to order this second list in reverse alphabetical order.

#Reverse the copied list
Fairfield_Prep_SubjectX.reverse()
#print reversed copied list
print(Fairfield_Prep_SubjectX)