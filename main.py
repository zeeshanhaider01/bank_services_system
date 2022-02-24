# from account_record import *
from creat_acont import creat_acount 
from sign_in import sign_in
from clear_console import *
clearConsole()
print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
print("                     ")
# json_read()
# print("acount_record: ",acount_record)
will=True
while will:
    clearConsole()
    print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
    print("                     ")
    print("                     For Login:press(1)") #21 space characters
    print("                     For signup: press(2)") #21 space characters
    print("                     For exit: press(3)") #21 space characters
    want=input("                     Press any of the above keys: ") #21 space characters
    if want=="1":
        clearConsole()
        print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
        print("                     ")
        sign_in()

    elif  want=="2":
        clearConsole()
        print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
        print("                     ")
        creat_acount()
    
    elif want=="3":
        # json_write()
        # print("                     acount_record: ",acount_record)
        clearConsole()
        print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
        print("                     ")
        print("                     Welcome any time!")
        will=False
    else:
        pass

