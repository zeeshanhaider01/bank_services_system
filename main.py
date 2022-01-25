from creat_acont import creat_acount 
from sign_in import sign_in
from clear_console import *
clearConsole()
print("Welcome to PAK Bank")
will=True
while will:
    print("For Login:press(1)")
    print("For signup: press(2)")
    print("For exit: press(3)")
    want=input("Press any of the above keys: ")
    if want=="1":
        clearConsole()
        sign_in()

    elif  want=="2":
        clearConsole()
        creat_acount()
    
    elif want=="3":
        clearConsole()
        print("Welcome any time!")
        will=False
    else:
        pass

