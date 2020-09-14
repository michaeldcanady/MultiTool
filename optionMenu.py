#############################
# Developed by Michael Canady
# September 12, 2020
#############################

import os
import xml.etree.ElementTree as ET
import sys
import customError
import login

class optionMenu():
    __slot__ = ["options"]
    def __init__(self):
         #creates a dictionary of usable programs and if they are selected or not
        self.options = {k.split(".")[0].lower():False for k in os.listdir("Options") if k.endswith(".exe")}
    def select(self,selection):
        if(selection.lower() == "start" and True not in self.options.values()):
            print("Can't Start")
        elif(selection.lower() == "start" and True in self.options.values()):
            print("starting",",".join([name for name,bool in self.options.items() if bool == True]))
            return False
        elif(selection.lower() not in self.options.keys()):
            print("Please make a valid selection")
        elif(self.options[selection.lower()] == False):
            self.options[selection.lower()] = True
        return True
    def main(self):
        print("\n".join(["[x] "+name if bool == True else "[ ] "+name for name,bool in self.options.items()]))
        choice = input("Choice: ")
        return self.select(choice)
# End of OptionMenu Class
class scripts():
    __slot__ = ["tree","root","script","version","scriptName","author","contributors","scriptType","executable"]
    scripts = {} # Dictionary of instances of scripts class, with if they are the current script or not EX OBJECT:Bool
    def __init__(self,script):
        self.version = script.find('version').text
        self.scriptName = script.find('scriptName').text
        self.author = script.find('author').text
        self.contributors = self.adjustcon([script.find('contributors').text])
        self.scriptType = script.find('scriptType').text
        self.executable = os.path.join("Options",self.scriptName,".exe")
    def adjustcon(self,contributors):
        if(len(contributors) > 1): #20 checks if selected list is greater than 1 element
            return (", ".join(contributors[:-1]) ,"and",contributors[-1]) #21 formats output -> Running: element,..., and element
        elif(contributors[0] == None):
            return None
        else: #22 if only one selection made
            return (", ".join(contributors))

def openingScreen(scripts): #19 formatting for to part that appears.
    for k in scripts.keys():
        if k.scriptType == "optionMenu":
            script, scripts[k] = k, True
    welcome = "{0} WELCOME TO {1} {0}".format("-"*48,script.scriptName)
    credit = welcome+"""\nVersion: {0}\nDeveloped by {1} With help from {2}
{3} DISCLAIMERS {3}\nVerify that all usernames and password entered are valid. If the script needs to be terminated press ctrl+C.
Select all needed programs, multitool will run them in proper order. Once complete the respective notes/logs will be stored in a folder.\n{4}""".format(script.version,script.author,script.contributors
                                                                                                                                                    ,"-"*int((len(welcome)-13)/2),"-"*len(welcome))
    return (credit)

if __name__ == "__main__":
    try:
        scripts.scripts = {scripts(k):False for k in ET.parse("scriptInfo.xml").getroot().findall('script')}
        screen = openingScreen(scripts.scripts)
        menu = optionMenu()
        deciding = True
        while deciding:
            os.system('cls||clear') # clears cmd for illusion of updating
            print(screen)
            deciding = menu.main()
        # need to add method by which to pass variables.
        lines = open("RunOrderList.txt","r")
        for line in lines:
            print(line)
        login.login()
    except KeyboardInterrupt: # catch exit command ctrl+C
        print("\nExiting {0}".format(next(k.scriptName for k,v in scripts.scripts.items() if v == True)))
        input("Press the enter key to continue...")
    except Exception as e: # Catches Unexpected exceptions
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
