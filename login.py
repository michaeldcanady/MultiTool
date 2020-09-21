import multiprocessing
import os
import getpass
import win32security
import os
import sys
import win32com.shell.shell as shell
import win32net
from subprocess import Popen, PIPE


def validateLogin(username,password):
        try:
            hUser = win32security.LogonUser (
                username,
                "SENSENET",
                password,
                win32security.LOGON32_LOGON_NETWORK,
                win32security.LOGON32_PROVIDER_DEFAULT
            )
        except win32security.error as e:
            return True # If login attemp failes
        else:
            return False # User exists in network

def login():
    invalidTech = True
    count = 0
    while count < 3:
        user = input("Please enter your username: ")
        password = getpass.getpass("Please enter your password: ")
        invalidTech = validateLogin(user, password)
        print(invalidTech)
        if invalidTech:
                count += 1
        else:
                break
    else:
        print("Username/password verified, beginning {0}".format("Time"))
    return user,password

print(login())
