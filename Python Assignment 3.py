#While loop(Number Guessing Game)

import random 
secret_number = random.randint(1, 10)
print(secret_number)



attempts = 3

x=1

while x<=attempts :
    
    Number=int(input("Guess the number (between 1 and 10):"))
   
    if Number> 10 or Number<1:

        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue
    elif Number>secret_number:
        print("Too high. Try again.")
        
    elif Number<secret_number:
        print("Too low. Try again.")
        
    elif Number==secret_number:
        print("Congratulations! You guessed the correct number.")
        break;

    x+=1
if x>attempts:
    print("Better luck next time!")


#For Loop:(Multiplication Table Generator)    

X=int(input("Enter the number for which you want the multiplication table:"))

for i in range(1,11):

    result=i*X

    print(i,"*", X, "=", result)



#Function:(BMI Calculator)

weight=float(input("Enter your weight in kg:"))

height=float(input("Enter your height in meters:"))



def calculate_bmi(weight, height):
    BMI = weight / height**2
    return BMI

X=calculate_bmi(weight,height)
print (round(X,2))
    
