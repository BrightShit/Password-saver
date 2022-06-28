
from tkinter import *
window = Tk()
window.geometry("550x500")
window.title("Password saver")
window.configure(bg="#34eb52")
#Labels and stuff
label_platform=Label(window,text="Platform")
label_title=Label(window,text="Password Saver",font=("Arial",30),bg='#00e5ff',fg="white")
label_email=Label(window,text="Enter Email/Username")
#Input fields
platform_=Entry(window,width=35,borderwidth=8)
Email = Entry(window,width=35,borderwidth=8)
label_password=Label(window,text="Enter Password")
Password=Entry(window,width=35,borderwidth=8)
# Getting the input from the user and store it in a variable
# name of the entry: Email, Password
def get_email_input():
    file = open("Passwords.txt",'a')
    Platform=platform_.get()
    email_info = Email.get()
    password_info = Password.get()
    file.write("Platform: "+Platform+" | Email: "+email_info+"| Password: "+password_info+"\n\n")
    file.close()
    Email.delete(0,END)
    Password.delete(0,END)
    platform_.delete(0,END)
def read_():
    reading=Tk()
    reading.configure(bg="#34eb52")
    reading.geometry("420x420")
    file1 = open("Passwords.txt","r")
    new_label=Label(reading,text=file1.read(),bg="#34eb52")
    new_label.pack()

# Button Logic
save=Button(window,padx=40,pady=4,text="Save",command=get_email_input,borderwidth=2.3)
read_passwords=Button(window,padx=10,pady=7,text="Show Passwords",command=read_)
# Placing all the different things on the screen
# And output to the user
label_platform.place(x=180,y=130)
platform_.place(x=180,y=150)
label_title.place(x=176,y=65)
label_email.place(x=180,y=190)
Email.place(x=180,y=210)
label_password.place(x=180,y=250)
Password.place(x=180,y=268)
save.place(x=233,y=335)
read_passwords.place(x=10,y=3)
window.mainloop()
