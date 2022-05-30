import time
#Main
def password():
    include_email_or_user = input("Do you want to save Email/Username? (Yes or no) \n") #Asks the user if he wants to add Username/Email
    if include_email_or_user.lower() == "yes": #if user input == "yes"
        Emails=input("Enter the Email/Username that you would like to save: \n") #Get the user input and store it
        Passwords=input("Enter the password that you would like to save: \n") #Get the user input and store it
        file=open("Password.txt", 'a') # Open/Create new text file called "Password.txt"
        file.write("Email/username: ") # Allow the user to read it more cleaner
        file.write(Emails) #Write the email/Username to the text file
        file.write("\n") #Add new line
        file.write("Password: ") #Allow the user to read it proprely and more cleaner
        file.write(Passwords) #Saves the password to the text file
        file.write("\n") #Add new line
        file.close #Close the file
        print("Password saved! ") #Let the user know that the password has been saved
        time.sleep(10)
    elif include_email_or_user.lower() == "no": #If user input == no
        Passwords=input("Enter the password that you would like to save: \n") #Get user input and store it
        file=open("Password.txt", 'a') #Open/ create new text file
        file.write("\n") # Add new line
        file.write("Password: ") # It will help the user to read proprely
        file.write(Passwords) #Writes the user password
        file.write("\n") #Add new line
        file.close #Close the file
        time.sleep(10)
    Add_another_password=input("Do you want to save another password?: \n")
    if Add_another_password.lower() == "yes":
        password()
    elif Add_another_password.lower() == "yes":
        print("See you soon!")
        time.sleep(5)

password()

    #End
