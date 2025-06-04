#This is a mini project where user can edit a folder with python

import os
import shutil

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

        file_path = input("Please enter file path: ")
        file_path = file_path.replace("\\", "/")

        print(file_path)

        if os.path.exists(file_path):
            items = os.listdir(file_path)

            for item in items:
                item_path = os.path.join(file_path, item)
                if os.path.isfile(item_path):
                    print(f"File: {item}")
                elif os.path.isdir(item_path):
                    print(f"Folder: {item}")
                else:
                    print(f"Unknown item: {item}")
        else:
            print("Please enter a valid file path")

    elif(user_option==2):
        folder_name=input("Please enter your new folder name: ") #Get new folder name from user
        folder_location=input("Please enter your new folder path: ") #Get location where user need to put the new folder
        folder_location=folder_location.replace("\\", "/")

        if os.path.exists(folder_location):
            folder_location=(folder_location + "\\" + folder_name)
            
            os.mkdir(folder_location)
            print("Successfully created a new folder as " + folder_name)
        else:
            print("Please enter a valid path.")

    elif (user_option==3):
        delete_folder_path=input("Please enter path of folder you need to delete: ")
        delete_folder_path=delete_folder_path.replace("\\","/")

        if os.path.exists(delete_folder_path):
            deleted_folder_path = delete_folder_path
            os.rmdir(delete_folder_path)

            print("Successfully removed "+ deleted_folder_path)
        
        else:
            print("Please enter a valid path.")

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