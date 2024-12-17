#!/usr/bin/env python3

from time import sleep
import os

# First Python program, and I just developed a bomb just to fuck with your system.
# Useful for pranking people. Or destroying one's system for revenge.

print("Initializing...")
sleep(0.5)
print("Hello, User!")
print("--My First Ever Exploit--")
print("--By: Vctor Castellar--")
yes = "Y"
no = "n"

# This function is where you plant the bomb/exploit
def bomb():
    print("The bomb has been planted.")
    for i in range(5, 0, -1): 
        print(f"Countdown: {i} seconds.")
        sleep(1)
    
    os.uname()
    os.system('ls -l -h')
    sleep(0.5)

    os.chdir('/home/vctor/folderforransomware')
    print(os.getcwd())
    print("Changed directory to target folder.")
    sleep(0.5)

    os.mkdir("SACMA")
    print("New folder made.")
    sleep(0.5)

    os.chdir("SACMA")
    print("Changed directory to new folder.")
    sleep(0.5)

    with open("SACMA Balls", "w+") as fd:
        fd.write("Gottem, baby!\n")
        fd.write("This is just a joke, worry not about it.\n")
        fd.write("Soon, you'll see me make amazing Python programs like these.\n")
        fd.write("Thanks for the program, asshole!\n")
    print("Created a file.")
    sleep(0.5)

    print("Have a nice day!")

# This if-else statement is made to confirm the activation and starting the program
# It's just like the fingerprint of the ssh command, but we've put it in a Python program
def start_program():
    program_start = input("Would you like to start the program? [Y/n] ")
    if program_start == yes:
        print("Planting the bomb...")
        sleep(8)
        bomb() # Calling the function...
    elif program_start == no: # This elif syntax is how you do if-else if statements
        print("Exiting...")
        sleep(3)
    else:
        print("Input the corresponding letter to start the program.")
        print("Y for yes, n for no.")
        start_program() # Recursion until the user provides the correct input

# You need this syntax to call the function and start the program
start_program()

# Things need to do in this code:
# 1. Build a bomb for the program.
# 	Q: What should the bomb contain?
# 	A: Either we give it a shot of pain or delete System32 for fun.
# 2. Test it on a dummy machine.
