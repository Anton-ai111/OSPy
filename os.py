import os 
import time

print("""

░█████╗░░██████╗
██╔══██╗██╔════╝
██║░░██║╚█████╗░
██║░░██║░╚═══██╗
╚█████╔╝██████╔╝
░╚════╝░╚═════╝░
""")

print("""
[1]Continue with the setup.
[2]Login in the setup.
[3]Quit.
""")

setup=input("[?]: ")

if setup=="1":
    name=input("Enter your name: ")
    password=input("Enter your password: ")

    with open("user/name.txt", "w") as f:
        f.writelines(name)
    
    with open("user/password.txt", "w") as f:
        f.writelines(password)

    print("SETUP COMPLETED!!!")
    time.sleep(3)
    os.startfile("main-os.py")

if setup=="2":

    login_name=open("user/name.txt")
    login_pass=open("user/password.txt")

    l_n=login_name.read()
    l_p=login_pass.read()
while True:
    login=input("Enter your password "+l_p)
    if login==l_p:
        print("True")
        os.startfile("main-os.py")
    else:
        print("wrong password!!!")



