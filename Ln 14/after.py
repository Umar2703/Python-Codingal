import os
s=input("do u want to shutdown y or n")
def shutdown(s):
    if s=="y":
        print("shutting down")
        os.system("shutdown/s /t 1")
    else:
        print("not shutting down")
shutdown(s)            