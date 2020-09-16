import os
import xml.etree.ElementTree as ET
import sys
from glob import glob
import scripts

def checkForOptions():
    return options

class optionMenu():
    __slot__ = ["options"]
    def __init__(self):
         #creates a dictionary of usable programs and if they are selected or not
        self.options = [k.split('\\')[-1].split(".")[0] for k in glob('Options/**/*.exe', recursive=True)]
        self.list = set(scripts.find('scriptName').text for scripts in ET.parse("scriptInfo.xml").getroot().findall('script'))
        self.options = {option.lower():False for option in self.options if option not in self.list}
    def menu(self): #3 when called displays GUI
        print("\n".join(["[x] "+name if bool == True else "[ ] "+name for name,bool in self.options.items()]))
    def select(self,selection):
        if(selection.lower() == "done" and True not in self.options.values()):
            print("You have not selected anything...")
            decicsion = input("Are you sure you are done (y/n): ")
            if(decicsion == "y"):
                return False
            else:
                pass
        elif(selection.lower() == "done" and True in self.options.values()):
            print("adding",",".join([name for name,bool in self.options.items() if bool == True]))
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

def openingScreen(scripts): #19 formatting for to part that appears.
    script = next(value for key,value in scripts.items() if value.scriptType=="scriptFinder")
    scriptName = script.scriptName
    welcome = "{0} WELCOME TO {1} {0}".format("-"*48,scriptName)
    credit = welcome+"""\nVersion: {0}\nDeveloped by {1} With help from {2}
{3} DISCLAIMERS {3}\nVerify that all usernames and password entered are valid. If the script needs to be terminated press ctrl+C.
Select all needed programs, multitool will run them in proper order. Once complete the respective notes/logs will be stored in a folder.\n{4}""".format(script.version,script.author,script.contributors
                                                                                                                                                    ,"-"*int((len(welcome)-13)/2),"-"*len(welcome))
    return (credit,scriptName)

if __name__ == "__main__":
    script = scripts.getScripts()
    screen,currentScript = openingScreen(scripts = script)
    menu = optionMenu()
    deciding = True
    print("exeChecker found programs not in MultiTool, would you like to add them?")
    response = input("Would you like to add any to MultiTool (y/n):")
    if(response == "y"):
        while deciding:
            os.system('cls||clear') # clears cmd for illusion of updating
            print(screen)
            deciding = menu.main()
        names = [name for name,bool in menu.options.items() if bool == True]
        scripts.addScript()
    else:
        sys.exit(0)
