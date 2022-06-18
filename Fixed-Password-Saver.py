import os
file = open("password.txt",'a')
def password():
    number__of__times= int(input("Enter the number of password that you want to save: \n"))
    for time in range(0,number__of__times):
        platfrom__=input("Enter the platform Example(Gmail/Google)\n")
        userName=input("Enter your username: \n")
        password__=input("Enter your password: \n")
        os.system("cls")
        file.write(platfrom__+":"+"\n"+"Username: "+userName+"\n"+"Password: "+password__+"\n"+"//////////////////////////////////////////////////////////////////////////////////////////"+"\n")

password()
print("Password successfully saved!")
os.startfile("password.txt")
file.close()
input()
