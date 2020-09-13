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
                None,
                password,
                win32security.LOGON32_LOGON_NETWORK,
                win32security.LOGON32_PROVIDER_DEFAULT
            )
        except win32security.error as e:
            return False # If login attemp failes
        else:
            return True # User exists in network

if __name__ == "__main__":
    invalidTech = True
    while invalidTech:
        user = input("Please enter your username: ")
        password = getpass.getpass("Please enter your password")
        invalidTech = validateLogin(user, password)
    else:
        print("Username/password verified, beginning {0}".format("Time"))
