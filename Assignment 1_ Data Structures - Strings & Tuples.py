#1. String Concatenation:
string1="Hello"

string2=input("Enter your name:")

result=string1+" "+string2

print(result)

string3=result+","+"welcome to Python programming"

print(string3)

#2. String Slicing and Indexing:

#a. Print the first character of the string.
print(string3[0])

#b. Print the last character of the string.

print(string3[-1])

#c. Print the first 5 characters of the string.
print(string3[0:5])

#d. Print the last 11 characters of the string.
print(string3[-11:])

#e. Print the string in reverse.
print(string3[::-1])

#f. Use slicing and print the word “Python” from the existing string.
print(string3[22:28])


#3. String Methods:
strM = "Python beginner tutorial"

#a. Convert the sentence to uppercase.

print(strM.upper())

#b. Convert the sentence to lowercase.

print(strM.lower())
# c. Use Capitalize and return the sentence to the original input form.
print(strM.capitalize())
#d. Count the total number of occurrences of character ‘t’ in the string.
print(strM.count("t"))

'''e. Replace all occurrences of “Python” with “Machine Learning” in the input string
strM = “Python beginner tutorial”'''

print(strM.replace("Python","Machine Learning"))


#Tuples (Creation, Modification and Access) :

tup1=(10, 20, 30)
tup2=(40, 50, 60)

#a. Concatenate the two tuples and store it in “t_combine”

t_combine=tup1+tup2
print(t_combine)

#b. Repeat the elements of “t_combine” 3 times
print(t_combine*3)

#c. Access the 3rd element from “t_combine”

print(t_combine[3])
#d. Access the first three elements from “t_combine”
print(t_combine[:3])

#e. Access the last three elements from “t_combine”

print(t_combine[-3:])


