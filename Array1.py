# QS1:Write a Python program to create an array of 5 integers and display the array items. Access individual elements through indexes.
'''
from array import *
arr=array('i',[1,3,5,7,9])
for i in arr:
    print(i)
print("Access first three data:")
print(arr[0])
print(arr[1])
print(arr[2])

# Qs:2  Write a Python program to append a new item to the end of the array.

from array import *
arr=array('i',[1,3,5,7,9])
arr.append(11)
print(arr)

#QS:3 Write a Python program to reverse the order of the items in the array.

# from array import *
# arr=array('i',[1,3,5,7,9,3,2,6])
# arr.reverse()
# print(arr)

arr=[1,2,3,4,5,6,7]
arr.reverse()
print(arr)

# 4. Write a Python program to get the length in bytes of one array item in the internal representation.

arr=[1,2,3,4,5,6,7]
print(len(arr))

# Qs:5Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array’s contents. Also, find the size of the memory buffer in bytes
from array import *
arr=array('i',[1,3,5,7])
print(arr.buffer_info())
print(arr.buffer_info()[1] * len(arr))

# Qs 6. Write a Python program to get the number of occurrences of a specified element in an array.

from array import *
arr=array('i',[1,3,5,3,7,3,3,3])
print(arr.count(3))

#Qs 7 Write a Python program to append items from inerrable to the end of the array.
arr=[1,2,3,4,5,6,7]
str12=["apple","banana","orange"]
arr.extend(str12)
print(arr)

# Qs
arr=[1,2,3,4,5]
arr.insert(1,9)
print(arr)

#Qs User provides two numbers and selects an operation (addition, subtraction, multiplication, division).
# Take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Choose an operation
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = int(input("Enter choice (1/2/3/4): "))

# Perform the selected operation
if operation == 1:
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif operation == 2:
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif operation == 3:
    result = num1 * num2
    print(num1, "*", num2, "=", result)
elif operation == 4:
    result = num1 / num2
    print(num1, "/", num2, "=", result)
else:
    print("Invalid Input")


# Qs: Make a game where the computer generates a random number, and the player has to guess it.
    
import random

# define range and max_attempts
lower_bound = 1
upper_bound = 1000
max_attempts = 10

# generate the secret number
secret_number = random.randint(lower_bound, upper_bound)

# Get the user's guess
def get_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("Invalid input. Please enter a number within the specified range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Validate guess
def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"

# track the number of attempts, detect if the game is over
def play_game():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)

        if result == "Correct":
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
            won = True
            break
        else:
            print(f"{result}. Try again!")

    if not won:
        print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    play_game()


'''

