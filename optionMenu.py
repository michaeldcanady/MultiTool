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
    def menu(self): #3 when called displays GUI
        print("\n".join(["[x] "+name if bool == True else "[ ] "+name for name,bool in self.options.items()]))
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
        self.menu()
        choice = input("Choice: ")
        return self.select(choice)
# End of OptionMenu Class
class scripts():
    __slot__ = ["tree","root","script","version","scriptName","author","contributors","scriptType","executable"]
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
    def getVersion(self):
        return self.version
    def setVersion(self,version):
        self.version = version
    def getName(self):
        return self.scriptName
    def setName(self,name):
        self.scriptName = name
    def getAuthor(self):
        return self.author
    def setAuthor(self,author):
        self.author = author
    def getContributors(self):
        return self.contributors
    def setContributors(self,contributors):
        self.contributors = contributors
    def getType(self):
        return self.scriptType
    def setTypes(self,type):
        self.scriptType = type
    def getExecutable(self):
        return self.executable
    def setExecutable(self,exe):
        self.executable = exe

def getScripts():
    scriptDict = {k.find('scriptName').text:scripts(k) for k in ET.parse("scriptInfo.xml").getroot().findall('script')}
    return scriptDict


def openingScreen(scripts): #19 formatting for to part that appears.
    script = next(value for key,value in scripts.items() if value.scriptType=="optionMenu")
    scriptName = script.scriptName
    welcome = "{0} WELCOME TO {1} {0}".format("-"*48,scriptName)
    credit = welcome+"""\nVersion: {0}\nDeveloped by {1} With help from {2}
{3} DISCLAIMERS {3}\nVerify that all usernames and password entered are valid. If the script needs to be terminated press ctrl+C.
Select all needed programs, multitool will run them in proper order. Once complete the respective notes/logs will be stored in a folder.\n{4}""".format(script.version,script.author,script.contributors
                                                                                                                                                    ,"-"*int((len(welcome)-13)/2),"-"*len(welcome))
    return (credit,scriptName)

if __name__ == "__main__":
    try:
        scripts = getScripts()
        screen,currentScript = openingScreen(scripts = scripts)
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
        print("Exiting {0}".format(currentScript))
        input("Press the enter key to continue...")
    except Exception as e: # Catches Unexpected exceptions
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
