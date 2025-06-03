#This is a mini project where user can edit a folder with python

import os

#Check user input is valid or not
def check_int(user_input):
    try:
        user_input = int(user_input)
        return True
    except ValueError:
        return False

print("Welcome to File Manager")

print("Please select the option to continue,")
print("     1) List Directory Files and Folders")
print("     2) Create a folder")
print("     3) Delete a folder")
print("     4) View Current Directory")
print("     5) Remove file")
print("     6) Rename file")
print("     7) Get file size")

user_option=input("Your option : ")

if check_int(user_option):
    user_option = int(user_option)
    if (user_option==1):
        file_path=r"C:\Users\Hiranya\Desktop"
        files =os.listdir(file_path)

        items = os.listdir(file_path)


        for item in items:
            item_path = os.path.join(file_path, item)  # Combine path with item
            if os.path.isfile(item_path):
                print(f"File: {item}")
            elif os.path.isdir(item_path):
                print(f"Folder: {item}")
            else:
                print(f"Unknown item: {item}")

    elif(user_option==2):
        print("Create a folder")

    elif (user_option==3):
        print("Delete a folder")

    elif(user_option==4):
        print("View current file directory")

    elif(user_option==5):
        print("Remove file")

    elif (user_option==6):
        print("Rename file")

    elif(user_option==7):
        print("Get file size")

else:
    print("Please enter a valid input.")