import os

while True:
    os.system("clear")
    print("[1] time to Bulk sms\n[2] Github user info")
    a = input("[>] Select Your Option: ") 

    if a == "1":
        os.system("python3 sms.py")
        a=input()
    elif a == "2":
        os.system("python3 github.py")
        a=input()
    else:
        print("[x] Wrong Value Entered!")
        a=input()
