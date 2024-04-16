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

# TO-DO-LIST :

# importing the required modules  
import tkinter as tk                    # importing the tkinter module as tk  
from tkinter import ttk                 # importing the ttk module from the tkinter library  
from tkinter import messagebox          # importing the messagebox module from the tkinter library  
import sqlite3 as sql                   # importing the sqlite3 module as sql  
  
# defining the function to add tasks to the list  
def add_task():  
    # getting the string from the entry field  
    task_string = task_field.get()  
    # checking whether the string is empty or not  
    if len(task_string) == 0:  
        # displaying a message box with 'Empty Field' message  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
        # adding the string to the tasks list  
        tasks.append(task_string)  
        # using the execute() method to execute a SQL statement  
        the_cursor.execute('insert into tasks values (?)', (task_string ,))  
        # calling the function to update the list  
        list_update()  
        # deleting the entry in the entry field  
        task_field.delete(0, 'end')  
  
# defining the function to update the list  
def list_update():  
    # calling the function to clear the list  
    clear_list()  
    # iterating through the strings in the list  
    for task in tasks:  
        # using the insert() method to insert the tasks in the list box  
        task_listbox.insert('end', task)  
  
# defining the function to delete a task from the list  
def delete_task():  
    # using the try-except method  
    try:  
        # getting the selected entry from the list box  
        the_value = task_listbox.get(task_listbox.curselection())  
        # checking if the stored value is present in the tasks list  
        if the_value in tasks:  
            # removing the task from the list  
            tasks.remove(the_value)  
            # calling the function to update the list  
            list_update()  
            # using the execute() method to execute a SQL statement  
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:  
        # displaying the message box with 'No Item Selected' message for an exception  
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
# function to delete all tasks from the list  
def delete_all_tasks():  
    # displaying a message box to ask user for confirmation  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    # if the value turns to be True  
    if message_box == True:  
        # using while loop to iterate through the tasks list until it's empty   
        while(len(tasks) != 0):  
            # using the pop() method to pop out the elements from the list  
            tasks.pop()  
        # using the execute() method to execute a SQL statement  
        the_cursor.execute('delete from tasks')  
        # calling the function to update the list  
        list_update()  
  
# function to clear the list  
def clear_list():  
    # using the delete method to delete all entries from the list box  
    task_listbox.delete(0, 'end')  
  
# function to close the application  
def close():  
    # printing the elements from the tasks list  
    print(tasks)  
    # using the destroy() method to close the application  
    guiWindow.destroy()  
  
# function to retrieve data from the database  
def retrieve_database():  
    # using the while loop to iterate through the elements in the tasks list  
    while(len(tasks) != 0):  
        # using the pop() method to pop out the elements from the list  
        tasks.pop()  
    # iterating through the rows in the database table  
    for row in the_cursor.execute('select title from tasks'):  
        # using the append() method to insert the titles from the table in the list  
        tasks.append(row[0])  
  
# main function  
if __name__ == "__main__":  
    # creating an object of the Tk() class  
    guiWindow = tk.Tk()  
    # setting the title of the window  
    guiWindow.title("To-Do List Manager - JAVATPOINT")  
    # setting the geometry of the window  
    guiWindow.geometry("500x450+750+250")  
    # disabling the resizable option  
    guiWindow.resizable(0, 0)  
    # setting the background color to #FAEBD7  
    guiWindow.configure(bg = "#FAEBD7")  
  
    # using the connect() method to connect to the database  
    the_connection = sql.connect('listOfTasks.db')  
    # creating the cursor object of the cursor class  
    the_cursor = the_connection.cursor()  
    # using the execute() method to execute a SQL statement  
    the_cursor.execute('create table if not exists tasks (title text)')  
  
    # defining an empty list  
    tasks = []  
      
    # defining frames using the tk.Frame() widget  
    header_frame = tk.Frame(guiWindow, bg = "#FAEBD7")  
    functions_frame = tk.Frame(guiWindow, bg = "#FAEBD7")  
    listbox_frame = tk.Frame(guiWindow, bg = "#FAEBD7")  
  
    # using the pack() method to place the frames in the application  
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  
      
    # defining a label using the ttk.Label() widget  
    header_label = ttk.Label(  
        header_frame,  
        text = "The To-Do List",  
        font = ("Brush Script MT", "30"),  
        background = "#FAEBD7",  
        foreground = "#8B4513"  
    )  
    # using the pack() method to place the label in the application  
    header_label.pack(padx = 20, pady = 20)  
  
    # defining another label using the ttk.Label() widget  
    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Consolas", "11", "bold"),  
        background = "#FAEBD7",  
        foreground = "#000000"  
    )  
    # using the place() method to place the label in the application  
    task_label.place(x = 30, y = 40)  
      
    # defining an entry field using the ttk.Entry() widget  
    task_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "12"),  
        width = 18,  
        background = "#FFF8DC",  
        foreground = "#A52A2A"  
    )  
    # using the place() method to place the entry field in the application  
    task_field.place(x = 30, y = 80)  
  
    # adding buttons to the application using the ttk.Button() widget  
    add_button = ttk.Button(  
        functions_frame,  
        text = "Add Task",  
        width = 24,  
        command = add_task  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = delete_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 24,  
        command = delete_all_tasks  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close  
    )  
    # using the place() method to set the position of the buttons in the application  
    add_button.place(x = 30, y = 120)  
    del_button.place(x = 30, y = 160)  
    del_all_button.place(x = 30, y = 200)  
    exit_button.place(x = 30, y = 240)  
  
    # defining a list box using the tk.Listbox() widget  
    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 26,  
        height = 13,  
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#CD853F",  
        selectforeground = "#FFFFFF"  
    )  
    # using the place() method to place the list box in the application  
    task_listbox.place(x = 10, y = 20)  
  
    # calling some functions  
    retrieve_database()  
    list_update()  
    # using the mainloop() method to run the application  
    guiWindow.mainloop()  
    # establishing the connection with database  
    the_connection.commit()  
    the_cursor.close()  