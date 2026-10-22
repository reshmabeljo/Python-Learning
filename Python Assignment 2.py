#1. List Creation:

age_list=[18,25,28,32,40]
name_list=["Anu","Divya","Reshma","Manu","Wilson"]

#2. List Operations / Modifications:

#a. Append the string "Yazhini" to name_list.

name_list.append("Yazhini")

#Insert the element 30 at index 2 in age_list.

age_list[2]=30

#c. Remove the string "Yazhini" from name_list.

name_list.remove("Yazhini")

#Pop the last element from age_list.

age_list.pop(4)

#e. Extend the age_list with additional ages [29, 30, 26]

age_list.extend([29, 30, 26])

# f. Sort age_list in descending order.

age_list.sort(reverse=True)

#g. Find Max age, Min age and sum of all ages from age_list.

max(age_list)
min(age_list)
sum(age_list)

#3. Accessing List Elements:

#a. Print the first element of name_list.
name_list[0]

#b. Print the last element of name_list

name_list[-1]

# c. Print the elements from index 2 to index 4 in name_list

name_list[2:4]

#d. Print the elements of name_list in reverse order.


name_list[::-1]

#Dictionary (Creation, Modification and Access):

#a. Create a dictionary named student_marks that maps the names of five
#students to their marks (use scale of from 0 to 100).

student_marks={"Dona":89,"Geethu":78,"Jithin":90,"Aby":68,"Anju":92}


#b. Access and print the mark of a specific student, of your choice.

student_marks["Jithin"]

#c. Add a new student "Janani" with a mark of 80 to the student_marks dictionary.

student_marks["Janani"] = 80

#d. Update the mark of any one older student to 82.

student_marks["Geethu"] = 82

#e. Use the keys(), values(), and items() methods to print all keys, values, and
#key-value pairs in the student_marks dictionary.


print(student_marks.keys())

print(student_marks.values())

print(student_marks.items())

#Sets (Operations):

#a. Create a set called my_set with following values:
#['a','e','i','o','u','a','a','i']
#Analyse the output and provide explanation for the same.

my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}

print(my_set)

'''
Explanation:
- A set  stores only unique elements.
- Duplicate values such as 'a' and 'i' are  removed.
'''



#b. Attempt to change the value of my_set[4] = 's'. If code throws an error, provide
#an explanation.

my_set[4] = 's'

'''TypeError: 'set' object does not support item assignment'''
'''Sets are not indexed, so we cannot access elements using positions such as my_set[4]'''



#c. Create two sets:
#set1 with values: {1, 3, 5, 7, 9}
#set2 with values: {2, 3, 5, 8, 10}

set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

print("Set 1:", set1)
print("Set 2:", set2)

#d. Compute and print the union and intersection of set1 and set2.

print("Union:", set1.union(set2))

print("Intersection:", set1.intersection(set2))

#Operators & Conditional Statements :

score = int(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Please enter a score between 0 and 10.")
elif score > 7:
    print("Above Average:Keep it up!")
elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")
else:
    print("Below Average: Need to improve.")







